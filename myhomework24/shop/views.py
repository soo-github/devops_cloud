from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import ShopForm
from shop.models import Shop, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    shop_qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list': shop_qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    },)


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_shop = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect("shop:shop_detail", saved_shop.pk)
        else:
            form = ShopForm()

        return render(request, "shop/shop_form.html", {
            "form": form,
        })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_shop = form.save()
            messages.success(request, "포스팅을 수정했습니다.")
            return redirect("shop:shop_detail", saved_shop.pk)
        else:
            form = ShopForm(instance=shop)
        return render(request, "shop/shop_form.html", {
            "form": form,
            "shop": shop,
        })


def shop_delete(request: HttpRequest, pk: int) -> HttpResponse:
    raise NotImplementedError("삭제는 아직 구현하지 않았습니다...")