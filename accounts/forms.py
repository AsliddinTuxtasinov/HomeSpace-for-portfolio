from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput

# sign in
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 30,
        required=True,
        widget = TextInput(attrs = {
            'name' : 'username',
            'id' : 'username',
            'placeholder' : 'asliddindev@gmail.com',
            'class' : 'form-control'
        })
        )
    

    password = forms.CharField(
        required=True,
        widget = PasswordInput(attrs = {
            'name' : 'password',
            'id' : 'password',
            'placeholder' : 'password',
            'class' : 'form-control'
        })
        )

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length = 30,
        required = True,
        widget = TextInput(attrs = {
            'name' : 'username',
            'id' : 'username',
            'placeholder' : 'username',
            'class' : 'form-control'
        }))

    email = forms.CharField(
        max_length = 255,
        required = True,
        widget = EmailInput(attrs = {
            'name':'email',
            'id':'email',
            'placeholder':'asliddindev@gmail.com',
            'class':'form-control'
        }))

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget = TextInput(attrs = {
            'name':'first_name',
            'id':'first_name',
            'placeholder':'first_name',
            'class':'form-control'
        }))

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget = TextInput(attrs = {
            'name':'last_name',
            'id':'last_name',
            'placeholder':'last_name',
            'class':'form-control'
        }))

    password1 =forms.CharField(
        required=True,
        widget = PasswordInput(attrs = {
            'name':'password1',
            'id':'password1',
            'placeholder':'password',
            'class':'form-control'
        }))
    password2 =forms.CharField(
        required=True,
        widget = PasswordInput(attrs = {
            'name':'password2',
            'id':'password2',
            'placeholder':'repassword',
            'class':'form-control'
        }))