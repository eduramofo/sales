from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from signup.forms import SignupForm
from account.create_user import create_user


def home(request):
    initial = {}
    signup_form = SignupForm(initial=initial)
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            name = signup_form.cleaned_data['name']
            # waid = signup_form.cleaned_data['waid']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            create_user(name, username, email, password)            
            new_user_auth = authenticate(username=username, password=password)
            login(request, new_user_auth)
            message_text = 'Obrigado por se cadastrar. Você está logado.'
            messages.add_message(request, messages.INFO, message_text)
            success_url = reverse('core:home')
            return HttpResponseRedirect(success_url)
        else:
            message_text = 'Ocorreu um ERRO durante a criação do seu usuário!'
            messages.add_message(request,messages.ERROR, message_text)
    context = {
        'page_title': 'Faça seu Cadastro',
        'nav_name': 'signup_core',
        'signup_form': signup_form,
    }
    return render(request, 'signup/home/index.html', context)
