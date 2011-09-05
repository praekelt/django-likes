from secretballot.middleware import SecretBallotIpUseragentMiddleware


class SecretBallotUserIpUseragentMiddleware(SecretBallotIpUseragentMiddleware):
    def generate_token(self, request):
        if request.user.is_authenticated():
            return request.user.username
        else:
            return super(SecretBallotUserIpUseragentMiddleware, self).\
                    generate_token(request)
