from rest_framework import serializers
from .models import Post, UploadPhoto

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPhoto
        fields = '__all__'