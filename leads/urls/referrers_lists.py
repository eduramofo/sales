from django.urls import path, include

from leads.views import referrers_lists as views

urlpatterns = [
    path('leads/referrers/edit/<uuid:referrer_id>/', views.referrers_edit, name='leads_referrers_edit'),
    path('leads/referrers/t1/<uuid:referrer_id>/', views.referrers_t1, name='leads_referrers_t1'),
    path('leads/referrers/t2/<uuid:referrer_id>/', views.referrers_t2, name='leads_referrers_t2'),
    path('leads/referrers/t3/<uuid:referrer_id>/', views.referrers_t3, name='leads_referrers_t3'),
    path('leads/referrers/cnr/<uuid:referrer_id>/', views.referrers_cnr, name='leads_referrers_cnr'),
    path('leads/referrers/all/<uuid:referrer_id>/', views.referrers_all, name='leads_referrers_all'),
    path('leads/referrers/closed/<uuid:referrer_id>/', views.referrers_closed, name='leads_referrers_closed'),
    path('leads/referrers/opened/<uuid:referrer_id>/', views.referrers_opened, name='leads_referrers_opened'),
    path('leads/referrers/news/<uuid:referrer_id>/', views.referrers_news, name='leads_referrers_news'),
    path('leads/referrers/tentando/<uuid:referrer_id>/', views.referrers_tentando, name='leads_referrers_tentando'),
    path('leads/referrers/agendamento/<uuid:referrer_id>/', views.referrers_agendamento, name='leads_referrers_agendamento'),
    path('leads/referrers/follow-up/<uuid:referrer_id>/', views.referrers_follow_up, name='leads_referrers_follow_up'),
    path('leads/referrers/ganho/<uuid:referrer_id>/', views.referrers_ganho, name='leads_referrers_ganho'),
    path('leads/referrers/perdido/<uuid:referrer_id>/', views.referrers_perdido, name='leads_referrers_perdido'),
    path('leads/referrers/next/<uuid:referrer_id>/', views.referrers_next, name='leads_referrers_next'),
]
