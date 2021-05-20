from django.urls import path

from leads.actions import views

app_name = 'actions'

urlpatterns = [
    path('<uuid:lead_id>/t1/', views.t1, name='t1'),
    path('<uuid:lead_id>/t2/', views.t2, name='t2'),
    path('<uuid:lead_id>/t3/', views.t3, name='t3'),
    path('<uuid:lead_id>/schedule/', views.schedule, name='schedule'),
    path('<uuid:lead_id>/upload/', views.upload, name='upload'),
    path('<uuid:lead_id>/lost/', views.lost, name='lost'),
    path('<uuid:lead_id>/win/', views.win, name='win'),
    path('<uuid:lead_id>/jump/', views.jump, name='jump'),
    path('<uuid:lead_id>/lost-direct/', views.lost_direct, name='lost_direct'),
    path('<uuid:lead_id>/ultimatum/', views.ultimatum, name='ultimatum'),
    path('<uuid:lead_id>/invalid/', views.invalid, name='invalid'),
    path('<uuid:lead_id>/ghosting/', views.ghosting, name='ghosting'),
    path('<uuid:lead_id>/ghosting-2/', views.ghosting_2, name='ghosting_2'),
]
