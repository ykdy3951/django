from django import forms
from django.contrib.auth.hashers import check_password
from .models import Kuser


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Plz enter your email'
        },
        max_length=64, label='Email'
    )
    nickname = forms.CharField(
        error_messages={
            'required': 'Plz enter your nickname.'
        },
        max_length=32, label='Nickname'
    )
    password = forms.CharField(
        error_messages={
            'required': 'Plz enter your password.'
        },
        widget=forms.PasswordInput, label='Password'
    )
    re_password = forms.CharField(
        error_messages={
            'required': 'Plz enter your password again.'
        },
        widget=forms.PasswordInput, label='re_Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        nickname = cleaned_data.get('nickname')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if Kuser.objects.filter(email=email).exists():
            self.add_error(
                'email', 'This email has already been registered. Check again.')

        if Kuser.objects.filter(nickname=nickname).exists():
            self.add_error(
                'nickname', 'The nickname is already in use. Plz input another nickname.')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'Passwords are different.')
                self.add_error('re_password', 'Passwords are different.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                kuser = Kuser.objects.get(email=email)
            except Kuser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return

            if not check_password(password, kuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
