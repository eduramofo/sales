from django.urls import path
from leads import views

app_name = 'leads'
urlpatterns = [
    path('leads/', views.leads_list, name='list'),
    path('upload/', views.leads_upload, name='upload'),
]
