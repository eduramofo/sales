from django.urls import path, include

from leads.views import referrers as views

urlpatterns = [
    path('referrers/old/', views.referrers_old, name='referrers-old'),
    path('referrers/opened/', views.referrers, name='referrers-opened'),
    path('referrers/', views.referrers, name='referrers'),
    path('referrers/2/', views.referrers_2, name='referrers-2'),
    path('referrers/1/', views.referrers_1, name='referrers-1'),
    path('upload/', views.leads_upload, name='upload'),
]
