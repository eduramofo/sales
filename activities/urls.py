from django.urls import path
from activities.views import activities_views, activities_leads_views


app_name = 'activities'
urlpatterns = [
    
    # activities
    path('add/', activities_views.activity_add, name='add'),
    path('<uuid:activity_id>/update/', activities_views.activity_update, name='update'),
    path('', activities_views.activities_list, name='list'),

    # activities - leads
    path('through-lead/add/<uuid:lead_id>/', activities_leads_views.add_through_lead, name='add-through-lead'),
    path('through-lead/update/<uuid:activity_id>/', activities_leads_views.update_through_lead, name='update-through-lead'),

]
