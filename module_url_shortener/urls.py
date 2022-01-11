from django.conf.urls import include, url
from rest_framework import routers

from module_url_shortener.views.ShortUrlViewset import ShortUrlViewset

router = routers.DefaultRouter()

router.register(r'short_url', ShortUrlViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
]
