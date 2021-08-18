from django.urls import path

from .views import main
from .views import statistics
from .views import settings
from .views import recommendation


app_name = 'core'
urlpatterns = [
    path('', main.index, name='home'),
    path('messages/', main.messages, name='messages'),
    path('statistics/', statistics.home, name='statistics'),
    path('statistics/balance/', statistics.balance, name='statistics_balance'),
    path('statistics/day-detail/', statistics.day_detail, name='statistics_day_detail'),
    path('statistics/day-detail/result/<str:dt>/', statistics.day_detail_result, name='statistics_day_detail_result'),
    path('settings/', settings.settings, name='settings'),
    path('indicacao/entrei/', recommendation.i_enrolled, name='recommendation_i_enrolled'),
    path('indicacao/conheci/', recommendation.i_knew, name='recommendation_i_knew'),
]
