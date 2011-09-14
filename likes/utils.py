from secretballot.models import Vote

from likes.signals import likes_enabled_test, can_vote_test
from likes.exceptions import LikesNotEnabledException, CannotVoteException


def _votes_enabled(obj):
    """See if voting is enabled on the class. Made complicated because
    secretballot.enable_voting_on takes parameters to set attribute names, so
    we can't safely check for eg. "add_vote" presence on obj. The safest bet is
    to check for the 'votes' attribute.

    The correct approach is to contact the secretballot developers and ask them
    to set some unique marker on a class that can be voted on."""
    return hasattr(obj.__class__, 'votes')


def likes_enabled(obj, request):
    if not _votes_enabled(obj):
        return False
    try:
        likes_enabled_test.send(obj, request=request)
    except LikesNotEnabledException:
        return False
    return True


def can_vote(obj, user, request):
    if not _votes_enabled(obj):
        return False

    # Common predicate
    if Vote.objects.filter(
        object_id=obj.id,
        token=request.secretballot_token
    ).count() != 0:
        return False

    try:
        can_vote_test.send(obj, user=user, request=request)
    except CannotVoteException:
        return False
    return True
