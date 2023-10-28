from django.shortcuts import redirect


def verifieduseronly(view):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:
            return view(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrapper_function

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func