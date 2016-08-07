from django import forms

from models import *


class Formcontato(forms.Form):
    first_name   = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nome *"}))
    last_name    = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Sobrenome *"}))
    email        = forms.EmailField( widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email *"}))
    phone        = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Tel."}))
    message_text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Mensagem *"}), max_length=500)

class Formemails(forms.Form):
    texto = forms.CharField(widget=forms.Textarea(attrs={"class":"form-conrtol", "placeholder":"Corpo da mensagem"}), max_length=1000)
    remetente = forms.ModelChoiceField(queryset=contato.objects.all(), widget=forms.Select(attrs={"class":"form-control","placeholder":"Contato"}))
    titulo_email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Assunto *"}))