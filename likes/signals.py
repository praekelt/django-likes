import django
import django.dispatch

if django.get_version().startswith("4."):
    likes_enabled_test = django.dispatch.Signal()
    can_vote_test = django.dispatch.Signal()

    # signal that is sent when an object is liked
    object_liked = django.dispatch.Signal()
else:
    likes_enabled_test = django.dispatch.Signal(providing_args=["instance", "request"])
    can_vote_test = django.dispatch.Signal(providing_args=["instance", "user", "request"])

    # signal that is sent when an object is liked
    object_liked = django.dispatch.Signal(providing_args=["instance", "request"])