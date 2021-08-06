from django.contrib.auth.models import User


def create_user(name, username, email, password):
    new_user = User.objects.create_user(
        first_name=name,
        username=username,
        email=email,
        password=password,
    )
    return new_user
