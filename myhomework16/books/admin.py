from django.contrib import admin
from books.models import Bookstore


class BookstoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bookstore)
