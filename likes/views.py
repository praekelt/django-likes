from django.http import HttpResponseNotFound

from secretballot import views
from secretballot.models import Vote


def can_vote(request, content_type, object_id, vote):
    return content_type.model_class().objects.get(id=object_id).\
            can_vote(request)[0]


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
            can_vote_test=can_vote,
            extra_context={
                'can_vote': False,
                'vote_status': 'voted',
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
            can_vote_test=can_vote
        )
