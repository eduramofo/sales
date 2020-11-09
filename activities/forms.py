import time

from django import forms
from activities.models import Activity, ACTIVITY_TYPE_CHOICES


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
