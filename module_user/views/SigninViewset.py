
from rest_framework_jwt.views import JSONWebTokenAPIView

from module_user.serializers.SigninSerializer import SigninSerializer


class SigninViewset(JSONWebTokenAPIView):
    serializer_class = SigninSerializer

    def post(self, request, *args, **kwargs):
        return super(SigninSerializer, self).post(request, *args, **kwargs)