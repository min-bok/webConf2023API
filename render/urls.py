from django.urls import path
from . import views

urlpatterns = [
    path('photo/', views.photo, name="photo")
]

