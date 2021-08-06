from django import forms
from leads import validators


class SignupForm(forms.Form):

    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex.: flavio.augusto'}
        ),
        max_length=100,
        required=True,
    )

    name = forms.CharField(
        label='Nome e Sobrenome',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex.: João da Silva'}
        ),
        max_length=500,
        required=True,
    )

    waid = forms.CharField(
        label='WhatsApp',
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex.: 5511987654321'}
        ),
        # validators=[validators.validate_telefone,],
        max_length=50,
        required=True,
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'email@exemple.com'}),
    )

    password = forms.CharField(
        label='Defina sua senha',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': '**************'}),
    )

    password_check = forms.CharField(
        label='Confirme sua senha',
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': '**************'}),
    )
