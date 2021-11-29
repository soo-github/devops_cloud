from django.db import models


class NewPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(verbose_name="Content")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
