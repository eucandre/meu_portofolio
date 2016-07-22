from django import forms
from models import *
class Formcontato(forms.Form):
    first_name   = forms.CharField(max_length=150)
    last_name    = forms.CharField(max_length=150)
    email        = forms.EmailField()
    phone        = forms.CharField(150)
    message_text = forms.CharField(widget=forms.Textarea)