from django.urls import path
from .views import post_like_unlike_view, posts_view

urlpatterns = [
    path('action/', post_like_unlike_view, name="post-like-unlike"),
    path('', posts_view, name="posts_all"),
]
