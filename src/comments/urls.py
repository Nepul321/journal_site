from django.urls import path
from .views import (
 CommentReplies

)

urlpatterns = [

 path('comments/<int:id>/', CommentReplies, name="comment_replies")

]