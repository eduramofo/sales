from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = 'registration/login.html'
