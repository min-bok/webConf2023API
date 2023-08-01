from asyncio import format_helpers
from django.db import models

class Post(models.Model):
    author = models.CharField("작성자", max_length=10, null=False)
    post_msg = models.TextField("내용", max_length=100, null=False)
    created_at = models.DateField("작성일", auto_now_add=True)

    def __str__(self):
        return self.post_msg
    
class UploadPhoto(models.Model):
    fileName = models.CharField("이미지명", max_length=30, null=False, default="name")
    files = models.FileField("이미지", upload_to="images", null=False, default="files")
    created_at = models.DateField("촬영일", auto_now_add=True)
    
    def __str__(self):
        return self.fileName