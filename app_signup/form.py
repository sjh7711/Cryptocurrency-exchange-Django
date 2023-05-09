from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AuthUser


class User_Form(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control form-control-user','placeholder':'이메일을 입력하세요.'}) )
    password1 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'비밀번호를 입력하세요.'}))
    password2 = forms.CharField(label='', max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder':'비밀번호를 재입력하세요.'}))
    username =  forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'아이디를 입력하세요.'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class Passwd_Form(forms.ModelForm):
    username =  forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'아이디를 입력하세요.'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control form-control-user','placeholder':'이메일을 입력하세요.'}) )

    class Meta:
        model = User
        fields = ['username', 'email']
        
        # widgets = {
        #     'user_id':forms.TextInput(attrs={
        #         'class':'form-control form-control-user',
        #         'placeholder':'아이디를 입력하세요.'
        #     }),
        #     'user_pn':forms.TextInput(attrs={
        #         'class':'form-control form-control-user',
        #         'placeholder':'휴대폰 번호를 입력하세요'
        #     }),
        #     'user_em':forms.TextInput(attrs={
        #         'class':'form-control form-control-user',
        #         'placeholder':'이메일을 입력하세요.'
        #     })
        # }