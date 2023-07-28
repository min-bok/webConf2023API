from rest_framework import viewsets
from .serializers import PostSerializer, PhotoSerializer
from .models import Post, UploadPhoto

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = UploadPhoto.objects.all()
    serializer_class = PhotoSerializer

