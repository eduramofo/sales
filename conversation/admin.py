from django.contrib import admin

from rangefilter.filter import DateRangeFilter

from conversation.models import Conversation


class ConversationAdmin(admin.ModelAdmin):

    list_filter = (
        ('created_at', DateRangeFilter),
        'type',
    )

    list_display = ('created_at', 'updated_at', 'type', 'lead',)

    autocomplete_fields = ['lead',]

admin.site.register(Conversation, ConversationAdmin)
