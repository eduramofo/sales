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
    
    # today
    path('today/', views.leads_list, name='today'),

    # add
    path('add/', views.lead_add, name='add'),
    
    # update
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),

    # go
    path('<uuid:lead_id>/go-to/', views.lead_go_to, name='go-to'),
    
    # upload / add
    path('upload/', views.leads_upload, name='upload'),

]
