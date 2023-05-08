from typing import Any, Optional
from django import forms
from .models import UserList


class User_Form(forms.ModelForm):
    user_pw_check = forms.CharField(label='', max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'비밀번호를 재입력하세요.'}))
    class Meta:
        model = UserList
        fields = ['user_id', 'user_pw', 'user_pw_check', 'user_pn', 'user_em']
        widgets = {
            'user_id':forms.TextInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'아이디를 입력하세요.'
            }),
            'user_pw':forms.PasswordInput(attrs={
                'class':'form-control form-control-user',
                'placeholder':'비밀번호를 입력하세요.'
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