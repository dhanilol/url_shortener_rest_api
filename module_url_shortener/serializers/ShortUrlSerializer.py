import datetime

from django.utils import timezone
from environ import environ
from rest_framework import serializers

from module_url_shortener.models.ShortUrl import ShortUrl
from module_url_shortener.helper import create_random_code

env = environ.Env()


class ShortUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = [
            'id', 'original_url', 'custom_url', 'short_url', 'expiration', 'user'
        ]
        read_only_fields = ('created', 'updated')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = env('BASE_URL')

    def validate(self, attrs):
        if not self.instance:
            if 'original_url' not in attrs:
                raise serializers.ValidationError({'original_url': 'Not Found'})

            if 'custom_url' in attrs:
                custom_url = '/u/{}'.format(attrs['custom_url'].replace(" ", "_"))
                q = self.Meta.model.objects.filter(custom_url=custom_url)

                if q.count() > 0:
                    if q.first().is_expired is False:
                        raise serializers.ValidationError({'custom_url': 'Already in use'})
                    if q.first().is_expired:
                        q.first().delete()
                else:
                    attrs['short_url'] = '{}{}'.format(self.base_url, custom_url)
                    attrs['custom_url'] = custom_url

            if 'short_url' not in attrs and 'custom_url' not in attrs:
                short_url = self.create_short_url()
                attrs['short_url'] = short_url

            if 'expiration' in attrs:
                if attrs['expiration'] < timezone.now():
                    raise serializers.ValidationError({'expiration': 'Expiration can not be prior to today'})
            else:
                attrs['expiration'] = (timezone.now() + datetime.timedelta(days=7)).date()

        return attrs

    def create_short_url(self):
        random_code = create_random_code()
        short_url = '{}/u/{}'.format(self.base_url, random_code)

        if self.Meta.model.objects.filter(short_url=short_url).exists():
            return self.create_short_url()

        return short_url
