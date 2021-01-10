from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from leads.models import WhatsappTemplate

# python manage.py shell
# from leads.whatsapp.serialize import main
# main()

# python manage.py loaddata leads/fixtures/leads_whatsapp_template.json


def main():

    data = serializers.serialize(
        'json',
        WhatsappTemplate.objects.all(),
    )

    with open('leads/fixtures/leads_whatsapp_template.json', 'w', encoding='utf-8') as out:
        out.write(data)
