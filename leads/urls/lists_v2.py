from django.urls import path

from leads.views import lists as views

app_name = 'lists'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('all/', views.all, name='all'),
    path('news/', views.news, name='news'),
    path('schedules/', views.schedules, name='schedules'),
    path('opened/', views.opened, name='opened'),
    path('flow/', views.now, name='flow'),
    path('priorities/', views.priorities, name='priorities'),
    path('ultimatum/', views.priorities, name='ultimatum'),
    path('ghosting/', views.ghosting, name='ghosting'),
    path('ghosting-2/', views.ghosting_2, name='ghosting_2'),
    path('off/', views.off, name='off'),
    path('off-2/', views.off_2, name='off_2'),
]
