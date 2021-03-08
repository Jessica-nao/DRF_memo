from posts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Fragment


class FragmentSerializer(serializers.ModelSerializer):
    member = UserSerializer()

    class Meta:
        fields = ('__all__')
        model = Fragment

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username','email')