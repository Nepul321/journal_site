from django.urls import path
from .views import post_like_unlike_view

urlpatterns = [
    path('action/', post_like_unlike_view, name="post-like-unlike"),
]
