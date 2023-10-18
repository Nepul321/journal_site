from django.shortcuts import render

def AllArticles(request, *args, **kwargs):
    template = "global.html"
    context = {

    }

    return render(request, template, context)