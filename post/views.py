from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer, PhotoSerializer
from .models import Post, UploadPhoto

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def index_reset(request):
        records = Post.objects.all()
        index = 1
        for record in records:
            old_record = Post.objects.get(id=record.id)
            record.id = index
            old_record.delete()
            record.save()
            index = index + 1

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            self.index_reset()
            return Response({"message": "Operate successfully"}, status=status.HTTP_201_CREATED)
        else:
            print("실패")
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = UploadPhoto.objects.all()
    serializer_class = PhotoSerializer