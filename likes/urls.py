from django.conf.urls import patterns, url

urlpatterns = patterns(
    'likes.views',
    url(r'^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)$', 'like',
        name='like'),
)
