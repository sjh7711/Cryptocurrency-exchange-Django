from .models import UserList
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
from .form import UserForm, User_Form
=======
from .form import User_Form
>>>>>>> 2ea214c40537f790e5f85d441917e0b3f658310a

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
<<<<<<< HEAD
    return render(request, 'signup.html', {'form':form} )

@csrf_exempt
def login(request):
    form = UserForm()
    return render(request, 'login.html', {'form':form})
=======
    return render(request, 'signup.html', {'form':form} )
>>>>>>> 2ea214c40537f790e5f85d441917e0b3f658310a
