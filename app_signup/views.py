# from .models import UserList
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .form import User_Form, Passwd_Form
from django.contrib.auth.models import User
from .models import AuthUser

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        exists = User.objects.filter(username=request.POST['username'])
        if exists.exists():
            return render(request, 'exists.html')
        elif form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = User_Form()
    return render(request, 'sign-up.html', {'form':form} )


@csrf_exempt
def forgot(request):
    if request.method == 'POST':
        form = Passwd_Form(request.POST)
        getuser = AuthUser.objects.filter(username=request.POST['username'], email=request.POST['email'],)
        if getuser.exists():
            passwd = list(getuser.values_list('password', flat=True))[0]
            return render(request, 'get-passwd.html', {'passwd':passwd})
    else:
        form = Passwd_Form()
    return render(request, 'forgot-passwd.html', {'form':form} )