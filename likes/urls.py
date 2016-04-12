try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

from likes.views import like

urlpatterns = [
    url(r'^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)$', like,name='like'),
]
