from django.shortcuts import render, redirect
from .models import Post
from users.decorators import verifieduseronly
from .forms import PostCreateForm
from django.core.paginator import Paginator

def AllArticles(request, *args, **kwargs):
    template = "global.html"
    stuff = Post.objects.all()
    p = Paginator(stuff, 15)
    page = request.GET.get('page')
    qs = p.get_page(page)
    nums = "a" * qs.paginator.num_pages
    context = {
      'qs' : qs,
      'nums' : nums
    }

    return render(request, template, context)


def ArticleDetails(request, slug, *args, **kwargs):
    template = "article_detail.html"
    qs = Post.objects.filter(slug=slug)

    if not qs:
        return redirect('/all/')

    obj = qs.first()
    context = {
      'obj' : obj,
    }

    return render(request, template, context)

@verifieduseronly
def ArticleCreateView(request, *args, **kwargs):
    template = "article_create.html"
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/all/')
    context = {
        'form' : form,
    }

    return render(request, template, context)


@verifieduseronly
def ArticleUpdateView(request, id_, *args, **kwargs):
    template = "article_update.html"
    qs = Post.objects.filter(id=id_)

    if not qs:
        return redirect('/all/')

    obj = qs.first()
    if not request.user.is_superuser:
        if not obj.author == request.user:
            return redirect('/all/')
        
    form = PostCreateForm(instance=obj)
    if request.method == "POST":
        form = PostCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/articles/view/{obj.slug}/')
    context = {
        'form' : form,
    }

    return render(request, template, context)