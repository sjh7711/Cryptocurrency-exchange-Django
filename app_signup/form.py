from typing import Any, Optional
from django import forms
from .models import UserList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Form(UserCreationForm):
#    user_pw_check = forms.CharField(label='', max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'비밀번호를 재입력하세요.'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control form-control-user','placeholder':'이메일을 입력하세요.'}) )
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'휴대폰 번호를 입력하세요.'}))
    class Meta:
        model = User
        label = ''
        fields = ['username', 'password1', 'password2', 'phone', 'email']
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'아이디를 입력하세요.'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'비밀번호를 입력하세요.'
            }),
            'password2':forms.PasswordInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'비밀번호를 재입력하세요.'
            }),
        }

class Passwd_Form(forms.ModelForm):
    class Meta:
        model = UserList
        fields = ['user_id', 'user_pn', 'user_em']
        widgets = {
            'user_id':forms.TextInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'아이디를 입력하세요.'
            }),
            'user_pn':forms.TextInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'휴대폰 번호를 입력하세요'
            }),
            'user_em':forms.TextInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'이메일을 입력하세요.'
            })
        }