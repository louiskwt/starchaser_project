from doctest import Example
from django import forms
from .models import Member
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(widget=forms.PasswordInput, label="密碼")

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密碼", widget=forms.PasswordInput)
    password2 = forms.CharField(label="確認密碼", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': '用户名',
            'email': '電郵'
        }
        help_texts = {
            'username': None
        }
        error_messages = {
            'username': {
                'unique': "用户名已被使用"
            }
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("2次輸入的密碼不一樣，請再次輸入")
        return cd['password']

class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit('submit', '完成')
        )
    class Meta:
        model = Member
        fields = ('phone_num', 'date_of_birth', 'role', 'status', 'active')
        labels = {
            'phone_num': '電話號碼',
            'date_of_birth': '生日',
            # 'gender': '姓別',
            'role': '現狀',
            'status': '簡介',
            'active': '是否正在尋找學生/導師'
        }
        # widgets = {
        #     'gender': forms.RadioSelect() 
        # }