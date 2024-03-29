import time

from django import forms
from activities.models import Activity, ACTIVITY_TYPE_CHOICES
from leads import models as leads_models

class ActivityForm(forms.ModelForm):

    DONE_CHOICES = (
        (False, 'Não'),
        (True, 'Sim'),
    )

    lead = forms.CharField(
        label='Lead ID',
        required=True,
    )

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
        label='Data/hora',
        widget=forms.DateTimeInput(
            format='%Y-%m-%d %H:%M',
            attrs={
                'type': 'text',
            }
        ),
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 2, 'cols':60}),
        required=False,
    )

    done = forms.ChoiceField(
        label='Feita?',
        choices=DONE_CHOICES,
        required=True,
    )

    class Meta:
        
        model = Activity

        fields = [
            'lead',
            'type',
            'subject',
            'due_date',
            'note',
            'done',
        ]

    def clean_lead(self):
        return leads_models.Lead.objects.get(id=self.cleaned_data['lead'])
