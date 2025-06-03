from django.urls import path, include
from blog.views import hello_world

urlpatterns = [
    path('hello-world/', hello_world),
]
