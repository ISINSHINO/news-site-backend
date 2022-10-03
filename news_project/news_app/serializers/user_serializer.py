from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from news_app.models import User
from .post_serializer import PostSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, required=False)    

    class Meta:
        model        = User
        fields       = ('id', 'username', 'email', 'profile_image', 'posts', 'password')
        extra_kwargs = {
            'password':{
                'write_only':'True',
                'style': {'input_type': 'password'}
            }
        }
         
    def validate_password(self, value: str) -> str:
        return make_password(value)