from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    
    path('', views.index, name='home'),

    path('statistics/', views.statistics, name='statistics'),
    
    path('settings/', views.settings, name='settings'),

]
