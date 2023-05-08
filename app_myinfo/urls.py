from django.urls import path
from app_myinfo import views

urlpatterns = [
    path('', views.myinfo, name="myinfo"),
]

# Register your models here.


