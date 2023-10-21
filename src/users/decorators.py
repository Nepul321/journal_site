from django.shortcuts import redirect


def superuseronly(view):
    def wrapper_function(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        else:
            return view(request, *args, **kwargs)

    return wrapper_function