from django.urls import path
from .views import (
    CommentsView,
    CommentView,
    CommentCreateView,
    CommentReplyCreateView
)


urlpatterns = [
    path('', CommentsView, name="api-comments"),
    path('<int:id>/', CommentView, name="api-comment"),
    path('create/', CommentCreateView, name="api-comment-create"),
    path('<int:id>/create/', CommentReplyCreateView, name="api-comment-reply")
]
