from django.urls import path

from .views import main
from .views import statistics
from .views import settings
from leads.views import qualified, qualified_confirmed


app_name = 'core'
urlpatterns = [
    path('', main.index, name='home'),
    #path('', qualified, name='home'),
    path('confirmed/<uuid:qualified_id>/', qualified_confirmed, name='qualified_confirmed'),
    path('messages/', main.messages, name='messages'),
    path('statistics/', statistics.statistics, name='statistics'),
    path('settings/', settings.settings, name='settings'),
]
