from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(username = validated_data.get('username'))
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user=user)
        return {
            'refresh': str(refresh),
            'access_token': str(refresh.access_token),
            'username' : user.username,
        }