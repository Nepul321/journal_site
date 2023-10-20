from django.shortcuts import render
from .models import Post

def AllArticles(request, *args, **kwargs):
    template = "global.html"
    qs = Post.objects.all()

    context = {
      'qs' : qs,
    }

    return render(request, template, context)


def ArticleDetails(request, id, *args, **kwargs):
    template = "article_detail.html"
    qs = Post.objects.filter(id=id)

    obj = qs.first()
    context = {
      'obj' : obj,
    }

    return render(request, template, context)