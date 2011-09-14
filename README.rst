Django Likes
============
**Django app providing view interface to django-secretballot.**

.. contents:: Contents
    :depth: 5

Installation
------------

#. Install or add django-likes to your Python path.

#. Add ``likes`` to your ``INSTALLED_APPS`` setting.

#. Add ``django.core.context_processors.request`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting.

Usage
-----

django-likes provides an inclusion tag called ``likes`` which you can use to render a like button for any given object. The tag accepts as first argument the object on which the like should be applied, i.e.::

    {% load likes_inclusion_tags %}

    ...some html...

    {% likes object %}

    ...some more html...

``object`` here is any Django ORM object. In the background the like is uniquely addressed to the object using its content type and object id.

.. note::

    In order for the ``likes`` tag to work the request object needs to be available within the template's context. You have to use `RequestContext <https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext>`_ in your views to construct context ensuring the request objects is available as part of the context. (This is why ``django.core.context_processors.request`` is required to be set as a ``TEMPLATE_CONTEXT_PROCESSORS``.)
