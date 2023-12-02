import django
django.setup()

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()


class AccountForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
           'username',
           'name',
           'email',
           'profile_pic'
        )

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs= {'class' : 'form-control'}),
        }