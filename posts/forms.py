from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

    name = forms.CharField(label="", widget=forms.TimeInput(attrs={'placeholder': 'Name',}))
    body = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Comment'}))
