from django import forms

class LoginForm(forms.Form):
    用户名 = forms.CharField()
    密码 = forms.CharField(widget=forms.PasswordInput)