from django.shortcuts import redirect
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from module_url_shortener.models.ShortUrl import ShortUrl
from module_url_shortener.serializers.ShortUrlSerializer import ShortUrlSerializer


class RedirectViewset(APIView):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [AllowAny]
    ordering = '-id'

    def get(self, request, *args, **kwargs):
        url = request.get_full_path()
        short_url = ShortUrl.objects.filter(short_url=url)

        if short_url.count() == 0:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            if short_url.first().is_expired:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            original_url = short_url.first().original_url

        return redirect(original_url)
