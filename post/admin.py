from django.contrib import admin
from .models import Post, UploadPhoto
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Post)
admin.site.register(UploadPhoto)