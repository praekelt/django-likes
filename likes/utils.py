from django.contrib.contenttypes.models import ContentType
from secretballot.models import Vote

from likes.exceptions import CannotVoteException, LikesNotEnabledException
from likes.signals import can_vote_test, likes_enabled_test


def _votes_enabled(obj):
    """See if voting is enabled on the class. Made complicated because
    secretballot.enable_voting_on takes parameters to set attribute names, so
    we can't safely check for eg. "add_vote" presence on obj. The safest bet is
    to check for the 'votes' attribute.

    The correct approach is to contact the secretballot developers and ask them
    to set some unique marker on a class that can be voted on."""
    return hasattr(obj.__class__, "votes")


def is_ajax(meta):
    if "HTTP_X_REQUESTED_WITH" not in meta:
        return False

    if meta["HTTP_X_REQUESTED_WITH"] == "XMLHttpRequest":
        return True

    return False


def likes_enabled(obj, request):
    if not _votes_enabled(obj):
        return False
    try:
        likes_enabled_test.send(sender=obj.__class__, instance=obj, request=request)
    except LikesNotEnabledException:
        return False
    return True


def can_vote(obj, user, request):
    if not _votes_enabled(obj):
        return False

    # Common predicate
    if Vote.objects.filter(
        object_id=obj.pk, content_type=ContentType.objects.get_for_model(obj), token=request.secretballot_token
    ).exists():
        return False

    # The middleware could not generate a token, probably bot with missing UA
    if request.secretballot_token is None:
        return False

    try:
        can_vote_test.send(sender=obj.__class__, instance=obj, user=user, request=request)
    except CannotVoteException:
        return False
    return True
