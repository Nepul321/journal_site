from django.urls import path
from .views import (
 CommentReplies,
 CommentUpdate

)

urlpatterns = [

 path('comments/<int:id_>/', CommentReplies, name="comment_replies"),
 path('comments/<int:id>/update/', CommentUpdate, name="comment_update"),

]