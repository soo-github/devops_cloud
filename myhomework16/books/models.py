from django.db import models


class Bookstore(models.Model):
    product = models.CharField(max_length=50, db_index=True)
    price = models.CharField(max_length=11)
    description = models.TextField(blank=True)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

