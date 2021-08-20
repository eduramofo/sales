from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from event.models import Event


class EventAdmin(admin.ModelAdmin):

    search_fields = ('id', 'summary',)

    list_filter = (
        ('created_at', DateRangeFilter),
        'done',
    )
    
    list_display = ('created_at', 'updated_at', 'summary', 'lead', 'done',)

    autocomplete_fields = ['lead',]

admin.site.register(Event, EventAdmin)
