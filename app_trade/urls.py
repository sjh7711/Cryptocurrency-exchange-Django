from django.contrib import admin
from django.urls import path
from app_trade import views

urlpatterns = [
    path('', views.trade, name="trade"),
    path('submit/', views.submit, name="submit")
]