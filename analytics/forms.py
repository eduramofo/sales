from email.policy import default
from django import forms
from tempus_dominus.widgets import DatePicker
from analytics.constants import REPORT_CHOICES, REPORT_DEFAULT


datetime_picker = DatePicker(
    options={
        'useCurrent': False,
        'collapse': True,
        'locale': 'pt-BR',
        'format': 'DD/MM/YYYY',
    },
    attrs={
        'append': 'fa fa-calendar',
        'icon_toggle': True,
        'input_toggle': True,
        'input_group': True,
    },
)

class RangeDateSelectForm(forms.Form):

    report = forms.ChoiceField(
        label='Selecione o Relatório',
        choices=REPORT_CHOICES,
        required=True,
    )

    start_date = forms.DateField(
        label='Início da Data para Análise',
        input_formats=['%d/%m/%Y'],
        widget=datetime_picker,
        required=True,
    )

    end_date = forms.DateField(
        label='Fim da Data para Análise',
        input_formats=['%d/%m/%Y'],
        widget=datetime_picker,
        required=True,
    )
