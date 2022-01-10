from datetime import date, timedelta

from rest_framework import serializers, status
from rest_framework.response import Response

from module_url_shortener.models.ShortUrl import ShortUrl
from module_url_shortener.helper import create_random_code


class ShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = [
            'id', 'original_url', 'custom_url', 'short_url', 'expiration', 'user'
        ]
        read_only_fields = ('created', 'updated')

    def create(self, validated_data):
        if 'original_url' not in validated_data:
            return Response("{'original_url': 'Not Found'}", status=status.HTTP_404_NOT_FOUND)
        else:
            self.create_shortened_url(validated_data)

    def create_shortened_url(self, validated_data):
        if 'custom_url' in validated_data:
            q = self.Meta.model.objects.filter(custom_url=validated_data['custom_url'])

            if q.count() == 0:
                validated_data['short_url'] = validated_data['custom_url']
        else:
            if 'short_url' not in validated_data:
                random_code = create_random_code()
                if self.Meta.model.objects.filter(short_url=random_code).exists():
                    return self.create_shortened_url(validated_data)

                validated_data['short_url'] = random_code

            if 'expiration' not in validated_data:
                validated_data['expiration'] = date.today() + timedelta(days=7)

        short_url = super(ShortUrlSerializer, self).create(validated_data)
        return short_url
