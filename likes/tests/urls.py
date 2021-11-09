from django.conf.urls import include, url

from likes import urls as likes_urls

urlpatterns = [url(r"^", include(likes_urls))]
