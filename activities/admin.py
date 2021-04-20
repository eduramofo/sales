from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from activities.models import Activity


class ActivitiesAdmin(admin.ModelAdmin):
    pass

    # search_fields = ('name',)

    # list_per_page = 30

    list_filter = (
        ('created_at', DateRangeFilter),
        'type',
    )

    list_display = ('created_at', 'updated_at', 'subject', 'lead',)

    autocomplete_fields = ['lead',]

admin.site.register(Activity, ActivitiesAdmin)