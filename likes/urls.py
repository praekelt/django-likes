from django.urls import re_path

from likes import views

urlpatterns = [re_path(r"^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)/$", views.like, name="like")]
