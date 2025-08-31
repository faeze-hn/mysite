from django import forms
from website.models import Contact, NewsLetter
from django.db import  models
class NameForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    subject = forms.CharField(max_length=225)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model=NewsLetter
        fields = '__all__'