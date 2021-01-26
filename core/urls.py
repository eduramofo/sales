from django.urls import path

from .views import main
from .views import statistics
from .views import settings

app_name = 'core'
urlpatterns = [
    # path('', main.index, name='home'),
    path('', statistics.statistics, name='home'),
    path('messages/', main.messages, name='messages'),
    path('statistics/', statistics.statistics, name='statistics'),
    path('settings/', settings.settings, name='settings'),
]
