from django import forms

class SignInForm(forms.Form):
    user_name = forms.CharField(label='UserName', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
