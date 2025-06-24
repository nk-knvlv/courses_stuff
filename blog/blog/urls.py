from django.urls import path, include
from .views import post_list, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
]
