from django.shortcuts import redirect


def superuseronly(view):
    def wrapper_function(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        else:
            return view(request, *args, **kwargs)

    return wrapper_function

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func