from django.shortcuts import render, redirect
from academy.models import Module


def home(request):
    modules = Module.objects.filter(active=True)
    current_module = modules.first()
    context = {
        'page_title': 'Página Inicial',
        'nav_name': 'core_home',
        'modules': modules,
    }
    # return render(request, 'academy/home/index.html', context)
    return redirect('academy:module_detail', url=current_module.url)


def module_detail(request, url):
    modules_ = Module.objects.filter(active=True)
    current_module = modules_.filter(url=url).first()
    # modules = []
    # for module in Module.objects.filter(active=True):
    #     submodules = module.submodule_set.filter(active=True)
    #     modules.append({'module': module, 'submodules': submodules})
    context = {
        'page_title': current_module.title,
        'nav_name': 'core_home',
        'modules': modules_,
        'current_module': current_module,
    }
    return render(request, 'academy/module_detail/index.html', context)








def audio_speechs(request):

    audio_speechs = [
        {'title': 'Wendrio Bicaio', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/1_wendrio_bicaio.mp3'},
        {'title': 'Tayana Carvalho', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/2_tayana_carvalho.mp3'},
        {'title': 'Tarek Omar', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/3_tarek_omar.mp3'},
        {'title': 'Mariana Nascimento', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/4_mariana_nascimento.mp3'},
        {'title': 'Wendrio Bicaio 2', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/5_wendrio_bicaio.mp3'},
        {'title': 'Roberto Korea (DI)', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/6_roberto_korea.mp3'},
        {'title': 'Giovana La Farina', 'src': 'https://edu-fontes.s3-eu-west-1.amazonaws.com/speechs/7_giovana_la_farina.mp3'},
    ]

    context = {
        'page_title': 'Gravações de Entrevistas em Áudios',
        'nav_name': 'core_home',
        'audio_speechs': audio_speechs,
    }

    return render(request, 'academy/audio_speechs/index.html', context)


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
    return render(request, 'academy/technique/technique_6/index.html', context)


def technique_7(request):
    context = {
        'page_title': 'Validação',
        'nav_name': 'core_home'
    }
    return render(request, 'academy/technique/technique_7/index.html', context)
