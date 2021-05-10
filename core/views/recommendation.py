import json

from django.shortcuts import HttpResponseRedirect
from django.views.defaults import HttpResponseNotFound
from leads.whatsapp.api import whatsapp_api_recommendation_i_enrolled, whatsapp_api_recommendation_i_knew


def i_enrolled(request):
    url = whatsapp_api_recommendation_i_enrolled()
    if url is None: return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponseRedirect(url)


def i_knew(request):
    url = whatsapp_api_recommendation_i_knew()
    if url is None: return HttpResponseNotFound('<h1>Page not found</h1>')
    return HttpResponseRedirect(url)
