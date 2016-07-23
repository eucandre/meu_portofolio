from django.shortcuts import render_to_response
from django.template import RequestContext
from app_portofolio.forms import *
from app_portofolio.models import *

def portofolio(request):
    if request.method == 'POST':
        form = Formcontato(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item  = contato(first_name = dados['first_name'], last_name = dados['last_name'], email=dados['email'], phone=dados['phone'], message_text=dados['message_text'])
            item.save()
            return render_to_response("salvo.html",{})
    else:
            form = Formcontato()
    return render_to_response("index.html",{"form": form}, RequestContext(request))
