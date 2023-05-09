from .models import UserList
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .form import User_Form, Passwd_Form
from django.contrib.auth.models import User

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
        getuser = UserList.objects.filter(user_id=request.POST['user_id'], user_pn=request.POST['user_pn'], user_em=request.POST['user_em'],)
        if getuser.exists():
            password = list(getuser.values_list('user_pw', flat=True))[0]
            return render(request, 'get-passwd.html', {'password':password})
    else:
        form = Passwd_Form()
    return render(request, 'forgot-passwd.html', {'form':form} )