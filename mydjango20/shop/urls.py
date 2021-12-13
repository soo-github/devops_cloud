from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("<int:pk>/", views.shop_detail, name="shop_detail"),
    path("new/", views.shop_new, name="shop_new"),
    path("", views.shop_list, name="shop_list"),
    path("edit/<int:pk>/", views.shop_edit, name="shop_edit"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
    path("<int:shop_pk>/review/new/", views.review_new, name="review_new"),
    path("<int:shop_pk>/review/<int:pk>/edit/", views.review_edit, name="review_edit"),
]
