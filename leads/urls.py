from django.urls import path
from leads import views


app_name = 'leads'
urlpatterns = [

    # list
    path('', views.leads_list, name='list'),
    path('novos/', views.leads_novos_list, name='novos-list'),
    path('agendamentos/', views.leads_agendamentos_list, name='agendamentos-list'),
    path('em-aberto/', views.leads_em_aberto_list, name='leads-em-aberto-list'),
    path('indicators/', views.leads_indicators_list, name='indicators-list'),
    # list - now
    path('now/', views.leads_now, name='now'),

    # next
    path('next/', views.lead_next, name='next'),

    # add
    path('add/', views.lead_add, name='add'),
    
    # update
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),
    path('<uuid:lead_id>/update/run-now/<str:lead_run_now>/', views.lead_update_run_now, name='update-run-now'),
    
    # upload / add
    path('upload/', views.leads_upload, name='upload'),

]
