from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'likes.views',
    url(r'^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)$', 'like',
        name='like'),
    url(r'^like/celery/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)$',
        'like_celery',
        name='like_celery'),
)
