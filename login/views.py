from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = 'login/index.html'
