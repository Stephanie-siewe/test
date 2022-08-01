from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label='USERNAME')
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='PASSWORD')
