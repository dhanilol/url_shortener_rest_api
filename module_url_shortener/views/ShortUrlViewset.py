from urllib.request import urlopen

from django.shortcuts import redirect
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from environ import environ
from module_url_shortener.models.ShortUrl import ShortUrl
from module_url_shortener.serializers.ShortUrlSerializer import ShortUrlSerializer

env = environ.Env()


class ShortUrlViewset(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [AllowAny]
    ordering = '-id'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_url = env('BASE_URL')

    def retrieve(self, request, pk=None):
        short_url = pk
        # short_url = '{}/{}'.format(self.base_url, short_url)

        url = ShortUrl.objects.filter(short_url=short_url)

        if url.count() == 0:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            if url.first().is_expired():
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            original_url = url.first().original_url

        return redirect(original_url)
