from django.http import HttpResponseNotFound

from secretballot import views
from secretballot.models import Vote

from likes.utils import can_vote


def can_vote_test(request, content_type, object_id, vote):
    return can_vote(
        content_type.model_class().objects.get(id=object_id),
        request.user,
        request
    )


def like(request, content_type, id, vote):
    # Crawlers will follow the like link if anonymous liking is enabled. They
    # typically do not have referrer set.
    if 'HTTP_REFERER' not in request.META:
        return HttpResponseNotFound()

    url_friendly_content_type = content_type
    content_type = content_type.replace("-", ".")
    if request.is_ajax():
        return views.vote(
            request,
            content_type=content_type,
            object_id=id,
            vote=vote,
            template_name='likes/inclusion_tags/likes.html',
            can_vote_test=can_vote_test,
            extra_context={
                'likes_enabled': True,
                'can_vote': False,
                "content_type": url_friendly_content_type
            }
        )
    else:
        # Redirect to referer but append unique number(determined
        # from global vote count) to end of URL to bypass local cache.
        redirect_url = '%s?v=%s' % (request.META['HTTP_REFERER'], \
                Vote.objects.count() + 1)
        return views.vote(
            request,
            content_type=content_type,
            object_id=id,
            vote=vote,
            redirect_url=redirect_url,
            can_vote_test=can_vote_test
        )
