from django.urls import path
from . import views
from .views import *

urlpatterns = [
<<<<<<< HEAD
    #path('test01datas/', views.getTestDatas, name="test01datas"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
=======
    path('signup/', views.signup, name='signup'), 
>>>>>>> 2ea214c40537f790e5f85d441917e0b3f658310a
]