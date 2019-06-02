from django import forms
from .models import Theme, Comment, Hashtag

class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['title', 'body', 'hashtags', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

