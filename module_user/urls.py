from django.conf.urls import include, url
from rest_framework import routers

from module_user.views.MeViewset import MeViewset
from module_user.views.SigninViewset import SigninViewset
from module_user.views.SignupViewset import SignupViewset

router = routers.DefaultRouter()

router.register(r'me', MeViewset)
router.register(r'signup', SignupViewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'signin', SigninViewset.as_view())
]
