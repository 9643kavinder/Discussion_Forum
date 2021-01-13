from rest_framework import serializers
from .models import CustomUser, Speciality, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['message', 'created_at']


