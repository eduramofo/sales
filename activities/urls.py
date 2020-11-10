from django.urls import path
from activities.views import activities_views, activities_leads_views


app_name = 'activities'
urlpatterns = [
    
    # activities
    path('add/', activities_views.activity_add, name='add'),
    path('<uuid:activity_id>/update/', activities_views.activity_update, name='update'),
    path('', activities_views.activities_list, name='list'),

    # activities - leads
    path('add/lead/<uuid:lead_id>/', activities_leads_views.activity_add, name='add-activity-by-lead'),

]
