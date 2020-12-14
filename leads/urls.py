from django.urls import path

from leads import views
from leads import views_referrers


app_name = 'leads'
urlpatterns = [

    # leads lists
    path('', views.leads_list, name='list'),
    path('news/', views.leads_news, name='news'),
    path('schedules/', views.leads_schedules, name='schedules'),
    path('opened/', views.leads_opened, name='opened'),
    path('now/', views.leads_now, name='now'),
    path('priorities/', views.leads_priorities, name='priorities'),

    # lead next
    path('next/', views.lead_next, name='next'),

    # lead add
    path('add/', views.lead_add, name='add'),
    
    # lead update
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),
    path('<uuid:lead_id>/update/run-now/<str:lead_run_now>/', views.lead_update_run_now, name='update-run-now'),
    
    # referrers: list
    path('referrers/old/', views.referrers_old, name='referrers-old'),
    path('referrers/', views_referrers.referrers, name='referrers'),

    # referrers: lead upload add by file
    path('upload/', views_referrers.leads_upload, name='upload'),

]
