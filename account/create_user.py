from django.contrib.auth.models import User


def create_user(name, username, email, password):
    new_user = User.objects.create_user(
        first_name=name,
        username=username,
        email=email,
        password=password,
    )
    new_user_setup(new_user)
    return new_user


def new_user_setup(user):
    # Criar o primeiro LEAD
    # Cria o 
    pass
