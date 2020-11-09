from django.urls import path
from activities import views as activities_views


app_name = 'activities'
urlpatterns = [
    path('add/', activities_views.activity_add, name='add'),
    path('<uuid:activity_id>/update/', activities_views.activity_update, name='update'),
    path('', activities_views.activities_list, name='list'),
]
