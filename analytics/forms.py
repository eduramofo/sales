from django import forms
from tempus_dominus.widgets import DatePicker


datetime_picker = DatePicker(
    options={
        'useCurrent': False,
        'collapse': True,
        'locale': 'pt-BR',
        'format': 'YYYY-MM-DD',
    },
    attrs={
        'append': 'fa fa-calendar',
        'icon_toggle': True,
        'input_toggle': True,
        'input_group': True,
    },
)


class DaySelectForm(forms.Form):
    day = forms.DateField(
        label='Dia para Análise',
        input_formats=['%d/%m/%Y'],
        widget=datetime_picker,
        required=True,
    )


class RangeDateSelectForm(forms.Form):
    start_day = forms.DateField(
        label='Início da Data para Análise',
        input_formats=['%d/%m/%Y'],
        widget=datetime_picker,
        required=True,
    )
    start_end = forms.DateField(
        label='Fim da Data para Análise',
        input_formats=['%d/%m/%Y'],
        widget=datetime_picker,
        required=True,
    )
