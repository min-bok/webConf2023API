from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, PhotoViewSet

app_name = "post"
router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'photo', PhotoViewSet)


urlpatterns = [
    path("", include(router.urls))
]
