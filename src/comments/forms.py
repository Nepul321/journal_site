from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

        widgets = {
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'cols' : '10', 'rows' : '5', 'placeholder' : 'Write a comment/reply'})
        }

        labels = {
            'content' : ''
        }