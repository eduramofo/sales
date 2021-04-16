from django.urls import path

from . import views


app_name = 'google_calendar'
urlpatterns = [
    path('oauth2/', views.oauth2, name='oauth2'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
]
