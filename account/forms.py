from dataclasses import fields
from django import forms
from .models import Member

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(widget=forms.PasswordInput, label="密碼")

class UserRegistrationForm(forms.Modelform):
    password = forms.CharField(label="密碼", widget=forms.PasswordInput)
    password2 = forms.CharField(label="確認密碼", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("2次輸入的密碼碼一樣，請再次輸入")
        return cd['password']

class MemberFrom(forms.ModelForm):
    class Meta:
        model = Member
        fields('phone_num', 'date_of_birth', 'gender', 'role', 'status', 'descritpion')