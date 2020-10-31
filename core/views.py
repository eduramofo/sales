from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView


@login_required()
def index(request):

    

    context = {
        'contacts': [],
        'whats_mensagem_padrao': '',
    }

    return render(request, 'core/index.html', context)
