from django.urls import path
from . import views


app_name = 'leads'
urlpatterns = [
    path('upload-contacts/', views.index, name='upload-contacts'),
]
