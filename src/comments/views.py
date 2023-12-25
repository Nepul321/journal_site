from django.shortcuts import render
from .models import Comment

# Create your views here.

def CommentReplies(request, id_, *args, **kwargs):
	template = "comment_replies.html"
	qs = Comment.objects.filter(id=id_)
	obj = qs.first()

	context = {
     'comment' : obj,
	}

	return render(request, template, context)