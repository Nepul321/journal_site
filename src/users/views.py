from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login,
    logout
)

from django.contrib.auth.forms import (
    AuthenticationForm,
)

from .decorators import unauthenticated_user

@unauthenticated_user
def LoginView(request, *args, **kwargs):
    template = "account_login.html"
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user =  form.get_user()
        login(request, user)
        return redirect('/')
    context = {
     'form' : form
    }

    return render(request, template, context)


@login_required
def LogoutView(request, *args, **kwargs):
    logout(request)
    return redirect('login-view')