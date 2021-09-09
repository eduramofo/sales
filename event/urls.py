from django.urls import path

from event import views

app_name = 'event'
urlpatterns = [
    path('list/', views.event_list_all, name='event_list_all'),
    path('list/open/', views.event_list_open, name='event_list_open'),
    path('list/open-next-24h/', views.event_list_open_next_24h, name='event_list_open_next_24h'),
    path('list/done/', views.event_list_done, name='event_list_done'),
    path('list/overdue/', views.event_list_overdue, name='event_list_overdue'),
    path('<uuid:event_id>/', views.event_update, name='event_update'),
]
