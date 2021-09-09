from django.urls import path, include

from leads import views

app_name = 'leads'

urlpatterns = [
    path('actions/<uuid:lead_id>/', include('leads.urls.actions'), name='actions'),
    path('lists/', include('leads.urls.lists_v2'), name='lists'),
    path('referrer/actions/<uuid:referrer_id>/', include('leads.urls.referrer_actions')),
    path('', include('leads.urls.lists')),
    path('', include('leads.urls.lead')),
    path('', include('leads.urls.referrers')),
]
