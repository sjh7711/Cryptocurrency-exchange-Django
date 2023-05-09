from django.contrib import admin
from django.urls import path
from app_main import views

urlpatterns = [
    path('', views.main, name="main"),
    path('try_login', views.try_login, name="try_login"),
    path('try_logout', views.try_logout, name="try_logout"),
    path('get_value', views.get_value, name='get_value'),
]

# Register your models here.


