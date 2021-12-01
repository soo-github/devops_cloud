from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
