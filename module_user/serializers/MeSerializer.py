from rest_framework import serializers

from module_user.models.User import User


class MeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'primary_email', 'primary_phone', 'password'
        ]
