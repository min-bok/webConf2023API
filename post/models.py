from django.db import models

class Post(models.Model):
    author = models.CharField("작성자", max_length=12, null=False)
    post_msg = models.TextField("내용", null=False)
    sticker = models.ImageField("스티커", blank=True, null=True)
    created_at = models.DateField("작성일", auto_now_add=True)

    def __str__(self):
        return self.post_msg