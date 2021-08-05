from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from . import authorize


@login_required()
def oauth2(request):
    authorization_url = authorize.authorize(request)
    return HttpResponseRedirect(authorization_url)


@login_required()
def oauth2callback(request):
    success_url = authorize.callback(request)
    return HttpResponseRedirect(success_url)


@login_required()
def oauth2success(request):
    oauth2success_url = reverse_lazy('core:home', args=())
    messages.add_message(request, messages.SUCCESS, 'Login realizado com sucesso no Google Calendar =)!')
    return HttpResponseRedirect(oauth2success_url)


@login_required()
def oauth2revoke(request):
    status_code = authorize.revoke()
    oauth2revoke_success_url = reverse_lazy('core:home', args=())
    if status_code == 200:
        messages.add_message(request, messages.SUCCESS, 'Acesso revogado com sucesso do token do Google Calendar.')
    else:
        messages.add_message(request, messages.ERROR, 'Ocorreu um erro.')
    return HttpResponseRedirect(oauth2revoke_success_url)
