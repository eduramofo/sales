import time

from django import forms
from activities.models import Activity, ACTIVITY_TYPE_CHOICES
from leads import models as leads_models


class ActivityForm(forms.ModelForm):

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
        label='Data/Hora',
        widget=forms.DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local',}
        ),
        required=True,
    )

    note = forms.CharField(
        label='Anotações',
        widget=forms.Textarea(attrs={'rows': 2, 'cols':60}),
        required=False,
    )

    class Meta:
        model = Activity
        fields = '__all__'

    def clean_lead(self):
        return leads_models.Lead.objects.get(id=self.cleaned_data['lead'])
