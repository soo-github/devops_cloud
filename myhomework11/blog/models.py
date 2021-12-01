from django.db import models
from blog.upload_to import uuid_name_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

