from django.shortcuts import render

# Create your views here.

def CommentReplies(request, *args, **kwargs):
	template = "comment_replies.html"
	context = {

	}

	return render(request, template, context)