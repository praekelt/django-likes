import django.dispatch

likes_enabled_test = django.dispatch.Signal(
    providing_args=['obj', 'request']
)
can_vote_test = django.dispatch.Signal(
    providing_args=['obj', 'user', 'request']
)
