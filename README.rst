Django Likes
============
**Django app providing view interface to django-secretballot.**

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add ``django-likes`` to your Python path.

#. Add ``likes`` to your ``INSTALLED_APPS`` setting.

#. Add ``django.core.context_processors.request`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting.

Usage
-----

Template Tags
~~~~~~~~~~~~~
django-likes provides an inclusion tag called ``likes`` which you can use to render a like button for any given object. The tag accepts as first argument the object on which the like should be applied, i.e.::

    {% load likes_inclusion_tags %}

    ...some html...

    {% likes object %}

    ...some more html...

``object`` here is any Django model object. In the background the like is uniquely addressed to the object using its content type and object id.

.. note::

    In order for the ``likes`` tag to work the request object needs to be available within the template's context. Thus you have to use `RequestContext <https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext>`_ in your views to construct context, which, combined with the ``django.core.context_processors.request`` context processor, will ensure the request object is available as part of the context.

Signals
~~~~~~~
To determine whether or not liking/voting should be enabled on an object, connect a signal handler to the ``likes.signals.likes_enabled_test`` signal, raising a ``likes.exceptions.LikesNotEnabledException`` if liking should be disabled. The default behaviour is that liking is enabled for all secretballot enabled objects.

To determine whether or not the current requesting user can vote, connect a signal handler to the ``likes.signals.can_vote_test`` signal, raising a ``likes.exceptions.CannotVoteException`` if the current user should not be allowed to vote (the handler receives a request object). The default behaviour is that all users can vote except if they have previously voted on the same object.

