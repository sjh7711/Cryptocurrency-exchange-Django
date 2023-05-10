from django.contrib import admin
from django.urls import path
from app_trade import views

urlpatterns = [
    path('', views.trade, name="trade"),
    path('nameScratch/', views.coin_name_data, name='nameScratch'),
    path('submit/', views.submit, name="submit"),
    # path('submit2/', views.submit2, name="submit2")
]