from django.contrib import admin
from django import forms
from leads.models import Lead
from rangefilter.filter import DateRangeFilter


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = '__all__'


class LeadAdmin(admin.ModelAdmin):

    change_form_template = "leads/admin/change_form.html"

    search_fields = ('name', 'tel', 'waid',)

    list_filter = (
        ('created_at', DateRangeFilter),
        ('next_contact', DateRangeFilter),
        'status',
        'quality',
        'indicated_by',
    )

    list_per_page = 8

    list_display = ('created_at', 'updated_at', 'name', 'status', 'indicated_by', 'quality', 'next_contact',)

    form = LeadForm

admin.site.register(Lead, LeadAdmin)
