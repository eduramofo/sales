from django.urls import path, include

app_name = 'integrations'
urlpatterns = [
    path('google-calendar/', include("integrations.google_calendar.urls")),
    path('telegram/', include("integrations.telegram.urls")),
]
