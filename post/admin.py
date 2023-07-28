from django.contrib import admin
from .models import Post, UploadPhoto

# Register your models here.
admin.site.register(Post)
admin.site.register(UploadPhoto)

