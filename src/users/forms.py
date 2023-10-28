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
           'first_name',
           'last_name',
           'email'
        )

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs= {'class' : 'form-control'})
        }