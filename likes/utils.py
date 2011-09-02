from likes.signals import can_vote_test
from likes.exceptions import CannotVoteException

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
