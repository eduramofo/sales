from django.urls import path

from event import views


app_name = 'event'
urlpatterns = [
    path('', views.event_list_all, name='event_list_all'),
    path('open/', views.event_list_open, name='event_list_open'),
    path('done/', views.event_list_done, name='event_list_done'),
    path('overdue/', views.event_list_overdue, name='event_list_overdue'),
    path('<uuid:event_id>/', views.event_update, name='event_update'),
]
