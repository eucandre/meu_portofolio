from django import forms
from models import *
class Formcontato(forms.Form):
    first_name   = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nome *"}))
    last_name    = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Sobrenome *"}))
    email        = forms.EmailField( widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email *"}))
    phone        = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Tel."}))
    message_text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Mensagem *"}), max_length=500)