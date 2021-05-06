from django.urls import path

from . import views

app_name = 'academy'
urlpatterns = [
    path('', views.home, name='home'),
]
