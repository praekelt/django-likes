Django Likes
============
**Django app providing view interface to django-secretballot.**

This app utilizes `django-secretballot <http://pypi.python.org/pypi/django-secretballot/>`_ to provide Facebook or Google+1 style item liking of Django model objects. Authenticated or anonymous users are allowed to like any given object only once.

.. contents:: Contents
    :depth: 5

Installation
------------
#. Install or add ``django-likes`` to your Python path.

#. Configure ``django-secretballot`` as described `here <http://pypi.python.org/pypi/django-secretballot/>`_

#. Add ``likes`` to your ``INSTALLED_APPS`` setting.
    
#. Add likes url include to your project's ``urls.py`` file:: 
    
    (r'^likes/', include('likes.urls')),

#. Add ``likes.middleware.SecretBallotUserIpUseragentMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting, i.e.::

    MIDDLEWARE_CLASSES = (
        ...other middleware classes...
        "likes.middleware.SecretBallotUserIpUseragentMiddleware",
    )

#. Add ``django.core.context_processors.request`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting, i.e.::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...other context processors...
        "django.core.context_processors.request",
    )

Usage
-----

Template Tags
~~~~~~~~~~~~~

{% like object %}
+++++++++++++++++
django-likes provides an inclusion tag called ``likes`` which renders a like button for any given object, displaying the number of likes and allowing users to like the object. The tag accepts as first argument the object for which to display and on which to apply likes, i.e.::

    {% load likes_inclusion_tags %}

    ...some html...

    {% likes object %}

    ...some more html...

``object`` here is any Django model object for which `django-secretballot <http://pypi.python.org/pypi/django-secretballot/>`_ voting has been enabled. In the background the like is uniquely addressed to the object using its content type and object id.

.. note::

    In order for the ``likes`` tag to work the request object needs to be available within the template's context. Thus you have to use `RequestContext <https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext>`_ in your views to construct context, which, combined with the ``django.core.context_processors.request`` context processor, will ensure the request object is available as part of the context.

The template tag supports AJAX style liking. To enable it you need ensure django-likes' static media is accessible, see `managing static files <https://docs.djangoproject.com/en/dev/howto/static-files/>`_. You also need to load jQuery somewhere in your template, e.g.::

    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.3/jquery.min.js"></script>

Signals
~~~~~~~
likes.signals.likes_enabled_test
++++++++++++++++++++++++++++++++
To determine whether or not liking/voting should be enabled on an object, connect a signal handler to the ``likes.signals.likes_enabled_test`` signal, raising a ``likes.exceptions.LikesNotEnabledException`` if liking should be disabled. The default behaviour is that liking is enabled for all secretballot enabled objects.

likes.signals.can_vote_test
+++++++++++++++++++++++++++
To determine whether or not the current requesting user can vote, connect a signal handler to the ``likes.signals.can_vote_test`` signal, raising a ``likes.exceptions.CannotVoteException`` if the current user should not be allowed to vote (the handler receives a request object). The default behaviour is that all users can vote except if they have previously voted on the object in question.

