from django.urls import path
from analytics import views


app_name = 'analytics'
urlpatterns = [
    path('select/', views.select, name='select'),
    path('production/<str:date_format>/<str:start_date>/<str:end_date>/', views.production, name='production'),
    path('balance/<str:date_format>/<str:start_date>/<str:end_date>/', views.balance, name='balance'),
]
