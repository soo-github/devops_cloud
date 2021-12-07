from django.conf import settings
from django.urls import path, include
from diary import views

app_name = "diary"

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('<int:pk>/',views.post_detail, name="post_detail")
]


