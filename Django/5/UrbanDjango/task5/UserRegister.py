from django import forms


class UserReg(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    age = forms.IntegerField(label='Введите свой возраст', min_value=0)
