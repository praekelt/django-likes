import django.dispatch

likes_enabled_test = django.dispatch.Signal(
    providing_args=['instance', 'request']
)
can_vote_test = django.dispatch.Signal(
    providing_args=['instance', 'user', 'request']
)

# signal that is sent when an object is liked
object_liked = django.dispatch.Signal(
    providing_args=["instance", "request"]
)
