from django.urls import path
from logout.views import logout_view


app_name = 'logout'
urlpatterns = [
    path('', logout_view, name='logout'),
]
