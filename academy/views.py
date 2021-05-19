from django.shortcuts import render


def home(request):
    context = {
        'page_title': 'Gravações de Entrevistas',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/index.html', context)


def technique_home(request):
    context = {
        'page_title': 'Técnica Visão Geral (Big Picture)',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/home/index.html', context)


def technique_1(request):
    context = {
        'page_title': 'Abertura/Apresentação',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_1/index.html', context)


def technique_2(request):
    context = {
        'page_title': 'Conexão/Investigação',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_2/index.html', context)


def technique_3(request):
    context = {
        'page_title': 'Decisão Imediata (D.I.)',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_3/index.html', context)


def technique_4(request):
    context = {
        'page_title': 'Speech',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_4/index.html', context)


def technique_5(request):
    context = {
        'page_title': 'Fechamento',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_5/index.html', context)


def technique_6(request):
    context = {
        'page_title': 'Referidos',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_5/index.html', context)


def technique_7(request):
    context = {
        'page_title': 'Validação',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_5/index.html', context)
