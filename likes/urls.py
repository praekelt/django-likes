from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'likes.views',
    url(r'^like/mb/(?P<id>\d+)/(?P<vote>\d+)$', 'like_modelbase', name='like_modelbase'),
    url(r'^like/mba/(?P<id>\d+)/(?P<vote>\d+)$', 'like_modelbase_ajax', name='like_modelbase_ajax'),
)
