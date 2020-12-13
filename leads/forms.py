import time

from django import forms
from leads.models import Lead


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
        model = Lead
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
        model = Lead
        fields = ['run_now',]


class UploadContactsForm(forms.Form):

    indicated_by = forms.CharField(
        label='Indicado por',
        max_length=1024,
    )

    indicated_by_datetime = forms.DateTimeField(
        label='Data e Hora da Indicação',
        required=False,
    )

    vcf_files = forms.FileField(
       label='Arquivos de contatos para upload',
       required=False,
    )

    def clean_indicated_by(self):
        
        now_milliseconds = str(int(round(time.time() * 1000)))
        
        indicated_by_cleaned_data = self.cleaned_data.get('indicated_by')

        indicated_by = str(indicated_by_cleaned_data + " (" + now_milliseconds + ")" )

        return indicated_by
