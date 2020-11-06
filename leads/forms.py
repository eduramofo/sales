import time

from django import forms
from leads.models import Lead


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = '__all__'


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
