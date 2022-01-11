from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from module_url_shortener.models.ShortUrl import ShortUrl
from module_url_shortener.serializers.ShortUrlSerializer import ShortUrlSerializer


class ShortUrlViewset(viewsets.ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    permission_classes = [AllowAny]
    ordering_fields = '__all__'
    search_fields = {'id', 'original_url', 'short_url'}

