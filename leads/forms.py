from django import forms
from leads import models as leads_models
from leads import validators
from tempus_dominus.widgets import DateTimePicker


datetime_picker = DateTimePicker(
    options={
        'useCurrent': False,
        'collapse': True,
        'stepping': 5,
        'locale': 'pt-BR',
        'format': 'DD/MM/YYYY HH:mm',
    },
    attrs={
        'append': 'fa fa-calendar',
        'icon_toggle': True,
        'input_toggle': True,
        'input_group': True,
    },
)

def get_line_group_choices(account):
    line_group_qs = leads_models.LineGroup.objects.filter(active=True, account=account).order_by('-default')
    line_group_choices = []
    if len(line_group_qs) > 0:
        for line_group in line_group_qs:
            line_group_id = str(line_group.id)
            if line_group.default:
                line_group_name = str(line_group.name) + ' (Padrão)'
            else:
                line_group_name = str(line_group.name)
            choice = (line_group_id, line_group_name)
            line_group_choices.append(choice)
    else:
        line_group_choices.append((None,'Sem Grupo'))
    return line_group_choices


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

    best_time_to_contact = forms.CharField(
        label='Melhor Horário p/ Contato',
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
            'best_time_to_contact',
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
            'line_group',
            'validation',
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
        label='Data/Hora [Indicação]',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=datetime_picker,
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

    validation = forms.ChoiceField(
        label='Validação',
        choices=leads_models.VALIDATION_CHOICES,
        required=True,
    )

    vcf_files = forms.FileField(
       label='Arquivos de contatos para upload (VCF)',
       required=False,
    )

    line_group = forms.ChoiceField(
        label='Grupo da Linha',
        choices=(('','')),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        account = kwargs.pop('account', None)
        self.account = account
        super(ReferrerForm, self).__init__(*args, **kwargs)
        self.fields['line_group'].choices = get_line_group_choices(account)


    def clean_lead(self):
        data_lead_id = self.cleaned_data['lead']
        lead = None
        if data_lead_id:
            lead = leads_models.Lead.objects.get(id=self.cleaned_data['lead'])
        return lead

    def clean_line_group(self):
        data_line_group_id = self.cleaned_data['line_group']
        line_group = None
        if data_line_group_id:
            line_group_qs = leads_models.LineGroup.objects.filter(active=True, account=self.account).filter(id=data_line_group_id)
            if (len(line_group_qs)) > 0:
                line_group = line_group_qs.first()
        return line_group


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


class ScheduleForm(forms.Form):

    due_date = forms.DateTimeField(
        label='Data/Hora [INÍCIO]',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=datetime_picker,
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(
            attrs={'rows': 2, 'cols':60}
        ),
        required=False,
    )
