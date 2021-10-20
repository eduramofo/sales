from datetime import timedelta
from django import forms
from event import models
from tempus_dominus.widgets import DateTimePicker

datetime_picker = DateTimePicker(
    options={
        'useCurrent': True,
        'collapse': False,
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

class EventForm(forms.ModelForm):
    
    DONE_CHOICES = (
        (False, 'Não'),
        (True, 'Sim'),
    )
    
    summary = forms.CharField(
        label='Assunto',
        required=True,
    )

    start_datetime = forms.DateTimeField(
        label='Data/Hora [INÍCIO]',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=datetime_picker,
        required=False,
    )

    end_datetime = forms.DateTimeField(
        label='Data/Hora [FIM]',
        required=False,
    )

    done = forms.ChoiceField(
        label='Feita?',
        choices=DONE_CHOICES,
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        required=False,
    )

    class Meta:
        model = models.Event
        fields = [
            'summary',
            'start_datetime',
            'end_datetime',
            'done',
            'note',
        ]

    def clean_end_datetime(self):
        cleaned_data_start_datetime =  self.cleaned_data['start_datetime']
        cleaned_data_end_datetime = cleaned_data_start_datetime + timedelta(minutes=35)
        return cleaned_data_end_datetime
