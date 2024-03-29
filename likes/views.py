import random

from django import template
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseNotFound
from secretballot import views

from likes import signals
from likes.utils import can_vote, is_ajax


def can_vote_test(request, content_type, object_id, vote):
    return can_vote(content_type.get_object_for_this_type(id=object_id), request.user, request)


def like(request, content_type, id, vote, template_name="likes/inclusion_tags/likes.html", can_vote_test=can_vote_test):
    # Crawlers will follow the like link if anonymous liking is enabled. They
    # typically do not have referrer set.
    if "HTTP_REFERER" not in request.META:
        return HttpResponseNotFound()

    url_friendly_content_type = content_type
    app, modelname = content_type.split("-")

    content_type = ContentType.objects.get(app_label=app, model__iexact=modelname)
    if is_ajax(request.META):
        likes_template = "likes/inclusion_tags/likes_%s.html" % modelname.lower()
        try:
            template.loader.get_template(likes_template)
        except template.TemplateDoesNotExist:
            likes_template = "likes/inclusion_tags/likes.html"

        response = views.vote(
            request,
            content_type=content_type,
            object_id=id,
            vote=int(vote),
            template_name=template_name,
            can_vote_test=can_vote_test,
            extra_context={
                "likes_enabled": True,
                "can_vote": False,
                "content_type": url_friendly_content_type,
            },
        )
    else:
        # Redirect to referer but append unique number (determined
        # from global vote count) to end of URL to bypass local cache.
        redirect_url = "%s?v=%s" % (request.headers['Referer'], random.randint(0, 10))
        response = views.vote(
            request,
            content_type=content_type,
            object_id=id,
            vote=int(vote),
            redirect_url=redirect_url,
            can_vote_test=can_vote_test,
        )

    signals.object_liked.send(
        sender=content_type.model_class(), instance=content_type.get_object_for_this_type(id=id), request=request
    )
    return response
