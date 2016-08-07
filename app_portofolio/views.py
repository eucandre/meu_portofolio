from django.contrib.auth.decorators import login_required
from django.http import Http404
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

#@login_required
@login_required
def dashboard(request):
    try:
        mensagens = contato.objects.all()
        tamanho = len(mensagens)
        dat = contato.objects.get(pk=len(contato.objects.all()))
        return render_to_response("administrativo/index.html",{"mensagens":mensagens, "tamanho":tamanho, "data":dat.data})
    except contato.DoesNotExist:
        raise Http404("Banco de dados vazio, sem contato para administrar!")


@login_required
def aconpanha(request, nr_item):
    try:
        msg = contato.objects.get(pk=nr_item)
    except contato.DoesNotExist:
        raise Http404()
    return render_to_response("administrativo/mensagens.html", {"item_mensagem":msg})

def envia_email(request):
    if request.method == "POST":
        form = Formemails(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            item  = emails(remetente = dados['remetente'],titulo_email = dados['titulo_email'],texto = dados['texto'])
            item.save()
            para = item.remetente
            assunto = item.texto
            oque = item.titulo_email
            #send_mail(oque, assunto, 'eucandre@gmail.com',[para])
            return render_to_response("salvo.html",{})
    else:
        form = Formemails()
    return render_to_response("administrativo/email.html",{"form": form}, RequestContext(request))