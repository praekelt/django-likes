from likes.signals import likes_enabled_test, can_vote_test
from likes.exceptions import LikesNotEnabledException, CannotVoteException

def likes_enabled(obj, request):
    try:
        likes_enabled_test.send(obj, request=request)
    except LikesNotEnabledException:
        return False
    return True

def can_vote(obj, user, request):
    # todo: need a check here to see if voting is enabled on the class. Made
    # complicated because secretballot.enable_voting_on takes parameters to set
    # method names, so we can't safely check for eg. "add_vote" method presence
    # on obj.
    try:
        can_vote_test.send(obj, user=user, request=request)
    except CannotVoteException as e:
        return False, e
    return True, None        
