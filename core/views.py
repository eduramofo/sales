from django.shortcuts import render


def index(request):

    context = {
        'contacts': [],
        'whats_mensagem_padrao': whats_mensagem_padrao,
    }

    return render(request, 'core/index.html', context)
