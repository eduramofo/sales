from django.urls import path

from . import views

app_name = 'academy'
urlpatterns = [
    path('', views.home, name='home'),
    path('technique/', views.technique_home, name='technique-home'),
    path('technique/1/', views.technique_1, name='technique-1'),
    path('technique/2/', views.technique_2, name='technique-2'),
    path('technique/3/', views.technique_3, name='technique-3'),
    path('technique/4/', views.technique_4, name='technique-4'),
    path('technique/5/', views.technique_5, name='technique-5'),
    path('technique/6/', views.technique_6, name='technique-6'),
    path('technique/7/', views.technique_7, name='technique-7'),
]
