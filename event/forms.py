from datetime import timedelta
from django import forms
from event import models


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
        label='Data e Hora do Início do Evento',
        widget=forms.DateTimeInput(
            format='%d/%m/%Y %H:%M',
            attrs={
                'type': 'text',
            }
        ),
        required=True,
    )

    end_datetime = forms.DateTimeField(
        label='Data e Hora do Fim do Evento',
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
