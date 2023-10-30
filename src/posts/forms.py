from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image_url', 'content', 'citations')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'image_url' : forms.FileInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'citations' : forms.Textarea(attrs={'class' : 'form-control'}),
        }