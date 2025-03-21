from django import forms

class LoginForms(forms.Form):
    usuario = forms.CharField(
        label='Nome de Login',
        required=True, 
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome de Login"
            }
        )
        )
    
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha"
            }
        )
        )
    
class CadastroForms(forms.Form):
    nome = forms.CharField(
        label = 'Nome Completo',
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: João da Silva"
            }
        )
    )

    email = forms.EmailField(
        label = 'Email',
        required=True,
        max_length=100,
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex:joaosilva@gmail.com"
            }
            )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha"
            }
        )
        )
    
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha mais uma Vez"
            }
        )
    )