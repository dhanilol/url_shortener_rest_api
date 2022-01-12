from datetime import datetime

from django.db import models

from module_user.models.User import User


class ShortUrl(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    original_url = models.URLField(max_length=200, null=False)
    custom_url = models.CharField(max_length=10, null=True)
    short_url = models.URLField(max_length=200, null=True)
    expiration = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='short_url', null=True)

    @property
    def is_expired(self):
        if datetime.now().date() > self.expiration.date():
            self.delete()
            return True
        return False
