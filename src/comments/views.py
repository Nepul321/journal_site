from django.shortcuts import render, redirect
from .models import Comment
from posts.models import Post
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

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
	form = CommentForm()
	context = {
     'comment' : obj,
     'post' : answer,
     'replies' : replies,
     'form' : form,
	}

	return render(request, template, context)

@login_required
def CommentUpdate(request, id, *args, **kwargs):
	template = "comment_update.html"
	qs = Comment.objects.filter(id=id)
	obj = qs.first()
	if request.user != obj.user:
		return redirect('/')
	form = CommentForm(instance=obj)
	if request.method == "POST":
		form = CommentForm(request.POST, instance=obj)
		if form.is_valid():
			form.save()
			return redirect(f'/comments/{obj.id}/')
	context = {
       'form' : form,
       'obj' : obj,
	}

	return render(request, template, context)
