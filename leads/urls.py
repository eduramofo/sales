from django.urls import path

from leads import views
from leads import views_leads_lists
from leads import views_referrers


app_name = 'leads'
urlpatterns = [

    # leads lists
    path('', views_leads_lists.all, name='list'),
    path('news/', views_leads_lists.news, name='news'),
    path('schedules/', views_leads_lists.schedules, name='schedules'),
    path('opened/', views_leads_lists.opened, name='opened'),
    path('now/', views_leads_lists.now, name='now'),
    path('priorities/', views_leads_lists.priorities, name='priorities'),

    # leads lists referrers
    path('leads/referrers/all/<uuid:referrer_id>/', views_leads_lists.referrers_all, name='leads_referrers_all'),
    path('leads/referrers/opened/<uuid:referrer_id>/', views_leads_lists.referrers_opened, name='leads_referrers_opened'),
    path('leads/referrers/news/<uuid:referrer_id>/', views_leads_lists.referrers_news, name='leads_referrers_news'),
    path('leads/referrers/tentando/<uuid:referrer_id>/', views_leads_lists.referrers_tentando, name='leads_referrers_tentando'),

    # lead next
    path('next/', views.lead_next, name='next'),

    # lead add
    path('add/', views.lead_add, name='add'),
    
    # lead update
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),
    path('<uuid:lead_id>/update/run-now/<str:lead_run_now>/', views.lead_update_run_now, name='update-run-now'),
    
    # referrers: list
    path('referrers/old/', views_referrers.referrers_old, name='referrers-old'),
    path('referrers/opened/', views_referrers.referrers, name='referrers-opened'),
    path('referrers/', views_referrers.referrers, name='referrers'),

    # referrers: lead upload add by file
    path('upload/', views_referrers.leads_upload, name='upload'),

]
