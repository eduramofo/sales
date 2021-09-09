from django.urls import path
from leads.views import actions as views

app_name = 'actions'

urlpatterns = [
    path('t1/', views.t1, name='t1'),
    path('t2/', views.t2, name='t2'),
    path('t3/', views.t3, name='t3'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/direct/', views.schedule_direct, name='schedule_direct'),
    path('add/', views.add, name='add'),
    path('add/upload/', views.add_upload, name='add_upload'),
    path('lost/', views.lost, name='lost'),
    path('off/', views.off, name='off'),
    path('win/', views.win, name='win'),
    path('jump/', views.jump, name='jump'),
    path('lost-direct/', views.lost_direct, name='lost_direct'),
    path('ultimatum/', views.ultimatum, name='ultimatum'),
    path('invalid/', views.invalid, name='invalid'),
    path('ghosting/', views.ghosting, name='ghosting'),
    path('ghosting-2/', views.ghosting_2, name='ghosting_2'),    
    path('whatsapp/<uuid:whatsapp_template_id>/', views.whatsapp_template, name='whatsapp'),
    path('activity/delete/<uuid:activity_id>/', views.activity_delete, name='activity_delete'),
]
