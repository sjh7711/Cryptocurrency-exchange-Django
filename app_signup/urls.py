from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #path('test01datas/', views.getTestDatas, name="test01datas"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    
]