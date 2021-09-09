from django.urls import path
from leads.views import referrer_actions as views

app_name = 'referrer_actions'

urlpatterns = [
    path('t1/', views.t1, name='t1'),
    path('t2/', views.t2, name='t2'),
    path('t3/', views.t3, name='t3'),
    path('ghosting-1/', views.ghosting_1, name='ghosting_1'),
    path('ghosting-2/', views.ghosting_2, name='ghosting_2'),
    path('lna/', views.lna, name='lna'),
    path('events/', views.events, name='events'),
    path('lost/', views.lost, name='lost'),
    path('ultimatum/', views.ultimatum, name='ultimatum'),
    path('off-1/', views.off_1, name='off_1'),
    path('off-2/', views.off_2, name='off_2'),
    path('invalid/', views.invalid, name='invalid'),
    path('win/', views.win, name='win'),
    path('all/', views.all, name='all'),
    # actions
    path('edit-leads/', views.edit_leads, name='edit_leads'),
    path('edit-card/', views.edit_leads, name='edit_card'),
    path('next/', views.next, name='next'),
]
