from django.shortcuts import render
from .models import Comment
from posts.models import Post

# Create your views here.

def CommentReplies(request, id_, *args, **kwargs):
	template = "comment_replies.html"
	qs = Comment.objects.filter(id=id_)
	obj = qs.first()
	qs_2 = Post.objects.all()
	answer = None
	for i in qs_2:
		if obj in i.comments.all():
			answer = i
	replies = obj.get_children()
	context = {
     'comment' : obj,
     'post' : answer,
     'replies' : replies,
	}

	return render(request, template, context)