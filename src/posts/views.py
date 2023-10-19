from django.shortcuts import render
from .models import Post

def AllArticles(request, *args, **kwargs):
    template = "global.html"
    qs = Post.objects.all()

    context = {
      'qs' : qs,
    }

    return render(request, template, context)