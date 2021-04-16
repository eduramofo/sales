from django.urls import path

from . import views


app_name = 'telegram'
urlpatterns = [
    path('telegram/', views.oauth2, name='telegram'),
]
