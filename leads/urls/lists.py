from django.urls import path

from leads.views import lists as views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('all/', views.all, name='list'),
    path('news/', views.news, name='news'),
    path('schedules/', views.schedules, name='schedules'),
    path('opened/', views.opened, name='opened'),
    path('now/', views.now, name='now'),
    path('priorities/', views.priorities, name='priorities'),
]
