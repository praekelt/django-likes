from django.http import HttpResponseBadRequest

from secretballot.middleware import SecretBallotIpUseragentMiddleware


class SecretBallotUserIpUseragentMiddleware(SecretBallotIpUseragentMiddleware):
    def process_request(self, request):
        if 'REMOTE_ADDR' in request.META and 'HTTP_USER_AGENT' in request.META:
            super(SecretBallotIpUseragentMiddleware, self).process_request(request)
        else:
            return HttpResponseBadRequest()

    def generate_token(self, request):
        if request.user.is_authenticated():
            return request.user.username
        else:
            return super(SecretBallotUserIpUseragentMiddleware, self).\
                    generate_token(request)
