from django import forms
from leads import models as leads_models


class LeadForm(forms.ModelForm):
    
    next_contact = forms.DateTimeField(
        label='Próximo Contato',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local',}
        ),
        required=False,
    )

    indicated_by_datetime = forms.DateTimeField(
        label='Data e hora da indicação',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local',}
        ),
        required=False,
    )

    run_now = forms.BooleanField(
        label='Lista de Agora?',
        required=False,
    )

    priority = forms.BooleanField(
        label='Prioridade?',
        required=False,
    )

    location = forms.CharField(
        label='Localização: País/Cidade',
        required=False,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 2, 'cols': 60}),
        required=False,
    )

    class Meta:
        model = leads_models.Lead
        fields = ['status', 'run_now', 'priority', 'name', 'next_contact',
        'indicated_by', 'indicated_by_datetime', 
        'tel', 'waid', 'note', 'location', 'gmt',
        ]


class LeadFormRunNow(forms.ModelForm):
    
    run_now = forms.BooleanField(
        label='Colocar na Lista de Execução de Agora?',
        required=False,
    )
    
    class Meta:
        model = leads_models.Lead
        fields = ['run_now',]


class ReferrerForm(forms.ModelForm):

    class Meta:

        model = leads_models.Referrer

        fields = [
            'referring_datetime',
            'gmt',
            'name',
            'lead',
            'short_description',
            'location',
        ]

    name = forms.CharField(
        label='Nome do referenciador',
        max_length=1024,
        required=True,
    )

    lead = forms.CharField(
        label='Lead ID',
        required=False,
    )

    referring_datetime = forms.DateTimeField(
        label='Data e hora da indicação',
        required=True,
    )

    location = forms.CharField(
        label='Localização da cidade/país',
        required=True,
    )

    short_description = forms.CharField(
        label='Descrição breve da "linha"',
        required=True,
    )

    gmt = forms.ChoiceField(
        label='GMT',
        choices=leads_models.GMT_CHOICES,
        required=True,
    )

    vcf_files = forms.FileField(
       label='Arquivos de contatos para upload (VCF)',
       required=False,
    )

    def clean_lead(self):
        data_lead_id = self.cleaned_data['lead']
        lead = None
        if data_lead_id:
            lead = leads_models.Lead.objects.get(id=self.cleaned_data['lead'])
        return lead
