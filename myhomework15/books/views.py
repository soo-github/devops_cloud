from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def bookstore_list(request: HttpRequest) -> HttpResponse:
    qs = Bookstore.objects.all()
    context = {
        "bookstore_list": qs,
    }
    return render(request, "books/bookstore_list.html", context)


def bookstore_detail(request: HttpRequest, pk: int) -> HttpResponse:
    bookstore = Bookstore.objects.get(pk=pk)
    context = {
        "bookstore": bookstore,
    }
    return render(request, "books/booksore_detail.html", context)
