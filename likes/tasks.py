from celery.task import task

from secretballot import views
from likes import signals


@task(ignore_result=True)
def like(request, content_type, id, vote, can_vote_test):
    views.vote(
        request,
        content_type=content_type,
        object_id=id,
        vote=vote,
        can_vote_test=can_vote_test
    )

    signals.object_liked.send(sender=content_type.model_class(),
        instance=content_type.get_object_for_this_type(id=id), request=request)
