try:
    from hashlib import md5
except ImportError:
    from md5 import md5

from django.http import HttpResponseBadRequest

from secretballot.middleware import SecretBallotIpUseragentMiddleware


class SecretBallotUserIpUseragentMiddleware(SecretBallotIpUseragentMiddleware):

    def generate_token(self, request):
        if request.user.is_authenticated():
            return request.user.username
        else:
            try:
                s = ''.join((request.META['REMOTE_ADDR'], request.META['HTTP_USER_AGENT']))
                return md5(s).hexdigest()
            except KeyError:
                return None
