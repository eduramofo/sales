from django import forms
from leads import models as leads_models
from leads import validators


class LeadForm(forms.ModelForm):
    
    next_contact = forms.DateTimeField(
        label='Próximo Contato',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local',}
        ),
        required=False,
    )

    run_now = forms.BooleanField(
        label='Agora?',
        required=False,
    )

    priority = forms.BooleanField(
        label='Prioridade?',
        required=False,
    )

    qualified = forms.BooleanField(
        label='Qualificado?',
        required=False,
    )

    location = forms.CharField(
        label='Localização',
        required=False,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        required=False,
    )

    class Meta:
        model = leads_models.Lead
        fields = [
            'status',
            'run_now',
            'priority',
            'qualified',
            'name',
            'nickname',
            'gender',
            'tel',
            'waid',
            'note',
            'location',
            'gmt',
        ]


class LeadSimpleForm(forms.ModelForm):

    lead_id = forms.CharField(
        label='Lead Id',
        required=True,
    )

    priority = forms.ChoiceField(
        label='Prioridade',
        choices=(
            (False, 'Não'),
            (True, 'Sim'),
        ),
        required=True,
    )

    location = forms.CharField(
        label='Localização',
        required=False,
    )

    note = forms.CharField(
        label='Anotações',
        required=False,
    )

    class Meta:
        model = leads_models.Lead
        fields = [
            'status',
            'name',
            'nickname',
            'gender',
            'priority',
            'tel',
            'waid',
            'note',
            'location',
            'gmt',
        ]


class LeadLostForm(forms.ModelForm):
    
    LEAD_STATUS_LOST_JUSTIFICATION_CHOICES = leads_models.LEAD_STATUS_LOST_JUSTIFICATION_CHOICES

    status_lost_justification = forms.ChoiceField(
        label='Justificativa da Perda',
        choices=LEAD_STATUS_LOST_JUSTIFICATION_CHOICES,
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        required=False,
    )

    class Meta:
        model = leads_models.Lead
        fields = ['name', 'status_lost_justification', 'note']


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


class QualifiedForm(forms.Form):

    name = forms.CharField(
        label='Nome e Sobrenome',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: João da Silva'}),
        max_length=500,
        required=True,
    )

    waid = forms.CharField(
        label='Celular/WhatsApp',
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: (31) 983433489'}),
        validators=[validators.validate_telefone,],
        max_length=50,
        required=True,
    )
