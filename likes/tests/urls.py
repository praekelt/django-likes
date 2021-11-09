from django.urls import include, path

from likes import urls as likes_urls

urlpatterns = [path('', include(likes_urls))]
