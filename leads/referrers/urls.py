from django.urls import path

from leads.actions import views_actions

app_name = 'leads'

urlpatterns = [
    path('<uuid:lead_id>/t1/', views_actions.t1, name='t1'),
    path('<uuid:lead_id>/t2/', views_actions.t2, name='t2'),
    path('<uuid:lead_id>/t3/', views_actions.t3, name='t3'),
    path('<uuid:lead_id>/schedule/', views_actions.schedule, name='schedule'),
    path('<uuid:lead_id>/upload/', views_actions.upload, name='upload'),
    path('<uuid:lead_id>/lost/', views_actions.lost, name='lost'),
    path('<uuid:lead_id>/win/', views_actions.win, name='win'),
]