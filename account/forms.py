from django import forms

# Login Form
class LoginForm(forms.Form):
    form_template_name = "login_snippet.html"
    username = forms.CharField()
    password = form.CharField(widget=forms.PasswordInput)