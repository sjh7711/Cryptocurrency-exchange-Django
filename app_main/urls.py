from django.contrib import admin
from django.urls import path
from app_main import views

urlpatterns = [
    path('', views.main, name="main"),
    path('try_login', views.try_login, name="try_login"),
    path('get_value', views.get_value, name='get_value'),
    # path('signup', views.coinlist, name="signup"),
    # path('trade', views.coinlist1, name="trade"),
]

# Register your models here.


