from django.shortcuts import render
from signup.forms import SignupForm


def home(request):

    signup_form = SignupForm()

    context = {
        'page_title': 'Faça seu Cadastro',
        'nav_name': 'signup_core',
        'signup_form': signup_form,
    }

    return render(request, 'signup/home/index.html', context)
