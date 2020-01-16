from django import forms


class AddFile(forms.Form):
    name = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
