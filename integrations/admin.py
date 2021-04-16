from django.contrib import admin

from integrations.models import GoogleApi


# Google API
class GoogleApiAdmin(admin.ModelAdmin):
    search_fields = ('description',)
    list_display = ('created_at', 'identifier', 'description',)

admin.site.register(GoogleApi, GoogleApiAdmin)
