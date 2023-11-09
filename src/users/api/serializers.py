import django
django.setup()
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'username',  
            'name',
            'is_author',
        ]