from django import forms
from blog.models import Comment
from django.db import  models
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','name', 'email', 'subject', 'message']
