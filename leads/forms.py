import time

from django import forms
from leads.models import Lead, Activity, ACTIVITY_TYPE_CHOICES


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
        label='Colocar na Lista de Execução de Agora?',
        required=False,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 4, 'cols':60}),
        required=False,
    )

    class Meta:
        model = Lead
        fields = '__all__'


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


class ActivityForm(forms.ModelForm):

    type = forms.ChoiceField(
        label='Tipo',
        choices=ACTIVITY_TYPE_CHOICES,
        required=True,
    )

    subject = forms.CharField(
        label='Assunto',
        required=True,
    )

    due_date = forms.DateTimeField(
        label='Data de Vencimento',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local',}
        ),
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 4, 'cols':60}),
        required=False,
    )

    class Meta:
        model = Activity
        fields = '__all__'
