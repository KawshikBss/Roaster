from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = '__all__'