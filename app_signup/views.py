from .models import UserList
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .form import UserForm, User_Form

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = User_Form(request.POST)
        exists = UserList.objects.filter(user_id=request.POST['user_id'])
        if exists.exists():
            return render(request, 'exists.html')
        elif form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = User_Form()
    return render(request, 'signup.html', {'form':form} )

@csrf_exempt
def login(request):
    form = UserForm()
    return render(request, 'login.html', {'form':form})
