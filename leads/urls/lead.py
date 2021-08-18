from django.urls import path

from leads.views import lead as views

urlpatterns = [
    path('next/', views.lead_next, name='next'),
    path('next-referrer/', views.lead_next_referrer, name='next_referrer'),
    path('add/', views.lead_add, name='add'),
    path('<uuid:lead_id>/update/', views.lead_update, name='update'),
]
