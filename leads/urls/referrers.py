from django.urls import path, include

from leads.views import referrers as views

urlpatterns = [
    path('referrers/select-current-line-group/', views.select_current_line_group, name='select-current-line-group'),
    path('referrers/', views.referrers, name='referrers'),
    path('referrers/2/', views.referrers_2, name='referrers-2'),
    path('referrers/1/', views.referrers_1, name='referrers-1'),
]
