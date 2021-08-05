from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from event.models import Event


class EventAdmin(admin.ModelAdmin):
    
    list_filter = (
        ('created_at', DateRangeFilter),
    )
    
    list_display = ('created_at', 'updated_at', 'summary', 'lead',)

    autocomplete_fields = ['lead',]

admin.site.register(Event, EventAdmin)
