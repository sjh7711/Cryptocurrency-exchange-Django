from django.contrib import admin
from django.urls import path
from app_trade import views

urlpatterns = [
    path('', views.trade, name="trade"),
    path('get_prices/', views.get_prices, name='get_prices'),
    path('trade_coin/',views.trade_coin, name='trade_coin'),
]