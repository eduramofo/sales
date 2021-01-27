from django.contrib.admin import AdminSite
from leads import admin as admin_leads
from leads import models as models_leads


class LeadAdminSite(AdminSite):
    site_header = "Wiser Leads"
    site_title = "Wiser Leads"
    index_title = "Seja-bem vindo ao Wiser Leads"

lead_admin_site = LeadAdminSite(name='admin_leads')


lead_admin_site.register(models_leads.Lead, admin_leads.LeadAdmin)
