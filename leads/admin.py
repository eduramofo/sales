from django.contrib import admin
from django import forms
from leads.models import Lead


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = '__all__'


class LeadAdmin(admin.ModelAdmin):

    # change_form_template = "cliente/signup/admin/change_form.html"

    search_fields = ('name', 'tel', 'waip',)

    list_filter = (
        'status',
        'quality',
        'indicated_by',
    )

    list_display = ('created_at', 'updated_at', 'name', 'indicated_by', 'quality',)

    form = LeadForm

admin.site.register(Lead, LeadAdmin)
