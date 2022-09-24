from django import forms
from .models import Member
from django.contrib.auth.models import User


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
    class Meta:
        model = Member
        fields = ('phone_num', 'telegram', 'mode', 'location', 'gender', 'date_of_birth', 'subject', 'role', 'status', 'description', 'price', 'active', 'referral')
        labels = {
            'phone_num': '可收 WhatsApp 的電話號碼',
            'telegram': 'Telegram ID （建議使用）',
            'mode': "教學模式",
            'location': '上課地點',
            'date_of_birth': '生日',
            'gender': '姓別',
            'subject': '科目',
            'role': '職業',
            'price': '收費 / 預算',
            'status': '簡介',
            'description': "詳細資料",
            'active': '是否正在尋找學生/導師',
            'referral': '會否考慮接受我們為你轉介 （成功轉介後會收取 $60 轉介費)'
        }
        widgets = {
            'phone_num': forms.TextInput(attrs={
                'placeholder': "63520220"
            }),
            'telegram': forms.TextInput(attrs={
                'placeholder': "@starchaser"
            }),
            'location': forms.TextInput(attrs={
                'placeholder': "中大新亞書院"
            }),
            'status': forms.TextInput(attrs={
                'placeholder': "中大心理學 Year 3 / 2022 DSE 英文 5**"
            }),
            'price': forms.TextInput(attrs={
                'placeholder': "100-250 / 義教 / 搵人一齊溫書"
            }),
            'date_of_birth': forms.DateInput(attrs=dict(type='date')),
            'gender': forms.RadioSelect(),
            'subject': forms.SelectMultiple(),
            'active': forms.RadioSelect(),
            'role': forms.RadioSelect(),
            'referral': forms.RadioSelect(),
            'description': forms.Textarea(attrs={
                'placeholder': "補底 / 追星"
            }),
        }
        help_texts = {
            "status": '最多50字，會展示在追星專頁的卡片/列表內去吸引人的注意',
            "description": '最多300字，只會展示在個人頁面內去幫人了解你更多'
        }
