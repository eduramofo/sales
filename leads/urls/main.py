from django.urls import path, include

from leads import views

app_name = 'leads'

urlpatterns = [
    path('actions/<uuid:lead_id>/', include('leads.urls.actions'), name='actions'),
    path('', include('leads.urls.lists')),
    path('', include('leads.urls.referrers_lists')),
    path('', include('leads.urls.lead')),
    path('', include('leads.urls.referrers')),
]