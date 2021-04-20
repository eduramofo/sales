from django.urls import path, include

from leads import views
from leads import views_update_v2
from leads import views_leads_lists
from leads import views_referrers_lists
from leads import views_referrers


app_name = 'leads'

urlpatterns = [
    path('actions/', include('leads.actions.urls'), name='actions'),
    # path('referrers/', include('leads.referrers.urls'), name='referrers'),






    # leads lists
    path('', views_leads_lists.all, name='list'),
    path('news/', views_leads_lists.news, name='news'),
    path('schedules/', views_leads_lists.schedules, name='schedules'),
    path('opened/', views_leads_lists.opened, name='opened'),
    path('now/', views_leads_lists.now, name='now'),
    path('priorities/', views_leads_lists.priorities, name='priorities'),

    # leads lists referrers

    ## edit
    path('leads/referrers/edit/<uuid:referrer_id>/', views_referrers_lists.referrers_edit, name='leads_referrers_edit'),

    ## Ts
    path('leads/referrers/t1/<uuid:referrer_id>/', views_referrers_lists.referrers_t1, name='leads_referrers_t1'),
    path('leads/referrers/t2/<uuid:referrer_id>/', views_referrers_lists.referrers_t2, name='leads_referrers_t2'),
    path('leads/referrers/t3/<uuid:referrer_id>/', views_referrers_lists.referrers_t3, name='leads_referrers_t3'),
    path('leads/referrers/cnr/<uuid:referrer_id>/', views_referrers_lists.referrers_cnr, name='leads_referrers_cnr'),

    path('leads/referrers/all/<uuid:referrer_id>/', views_referrers_lists.referrers_all, name='leads_referrers_all'),
    path('leads/referrers/closed/<uuid:referrer_id>/', views_referrers_lists.referrers_closed, name='leads_referrers_closed'),
    path('leads/referrers/opened/<uuid:referrer_id>/', views_referrers_lists.referrers_opened, name='leads_referrers_opened'),
    
    path('leads/referrers/news/<uuid:referrer_id>/', views_referrers_lists.referrers_news, name='leads_referrers_news'),
    path('leads/referrers/tentando/<uuid:referrer_id>/', views_referrers_lists.referrers_tentando, name='leads_referrers_tentando'),

    path('leads/referrers/agendamento/<uuid:referrer_id>/', views_referrers_lists.referrers_agendamento, name='leads_referrers_agendamento'),
    path('leads/referrers/follow-up/<uuid:referrer_id>/', views_referrers_lists.referrers_follow_up, name='leads_referrers_follow_up'),

    path('leads/referrers/ganho/<uuid:referrer_id>/', views_referrers_lists.referrers_ganho, name='leads_referrers_ganho'),
    path('leads/referrers/perdido/<uuid:referrer_id>/', views_referrers_lists.referrers_perdido, name='leads_referrers_perdido'),

    # leads lists referrers
    path('leads/referrers/next/<uuid:referrer_id>/', views_referrers_lists.referrers_next, name='leads_referrers_next'),

    # lead next
    path('next/', views.lead_next, name='next'),

    path('next-referrer/', views.lead_next_referrer, name='next_referrer'),

    # lead add
    path('add/', views.lead_add, name='add'),
    
    # lead update
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),

    # referrers: list
    path('referrers/old/', views_referrers.referrers_old, name='referrers-old'),
    path('referrers/opened/', views_referrers.referrers, name='referrers-opened'),
    path('referrers/', views_referrers.referrers, name='referrers'),
    path('referrers/2/', views_referrers.referrers_2, name='referrers-2'),

    # referrers: lead upload add by file
    path('upload/', views_referrers.leads_upload, name='upload'),

    # speech
    path('<uuid:lead_id>/speech/', views.speech_start, name='speech'),
    path('<uuid:lead_id>/speech-show/', views.speech_show, name='speech-show'),
    # path('<uuid:lead_id>/speech/', views.speech, name='speech'),

    # v2
    path('v2/', views_update_v2.update, name='update-v2'),
    path('v2/<uuid:lead_id>/', views_update_v2.update_content, name='update-v2-content'),

]
