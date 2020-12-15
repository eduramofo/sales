from leads.models import Lead, Referrer


def main():
    referrers()
    leads_priority()


def referrers():
    leads = Lead.objects.all()
    for lead in Lead.objects.all():
        create_or_get_referrer(lead)


def create_or_get_referrer(lead):
    name = lead.indicated_by
    referring_datetime = lead.indicated_by_datetime
    referrer_obj, c = Referrer.objects.get_or_create(
        name=name,
        gmt=-3,
        short_description='N/A',
        location='BR',
        referring_datetime=referring_datetime,
    )
    referrer_obj.leads.add(lead)
    referrer_obj.save()
    lead.indicated_by = ''
    lead.save()


def leads_priority():
    for le in Lead.objects.filter(quality__gte=2):
        le.priority = True
        le.save()
