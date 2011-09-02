import django.dispatch

can_vote_test = django.dispatch.Signal(providing_args=['obj', 'user', 'request'])
