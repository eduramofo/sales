from django.urls import path

from analytics import views

app_name = 'analytics'
urlpatterns = [
    path('', views.home, name='home'),
    path('today/', views.today, name='today'),
    path('this_week/', views.this_week, name='this_week'),
    path('day/select/', views.day_select, name='day_select'),
    path('day/result/<str:dt>/', views.day_result, name='day_result'),
    path('range/select/', views.range_select, name='range_select'),
    path('range/result/<str:dts>/<str:dte>/', views.range_result, name='range_result'),
    path('balance/', views.balance, name='balance'),
]
