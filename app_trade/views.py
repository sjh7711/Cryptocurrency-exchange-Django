from django.shortcuts import render
from django.views import View
from urllib.request import Request, urlopen
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt

import pyupbit
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyupbit


@csrf_exempt
def trade(request):
    return render(request, "trade.html")

def get_current_prices(ticker):
    price = pyupbit.get_current_price(ticker)
    return price

def get_prices(request):
    tickers = [
        "KRW-BTC", "KRW-ETH", "KRW-NEO", "KRW-MTL", "KRW-XRP",
        "KRW-ETC", "KRW-SNT", "KRW-WAVES", "KRW-XEM", "KRW-QTUM",
        "KRW-LSK", "KRW-STEEM", "KRW-XLM", "KRW-ARDR", "KRW-ARK",
        "KRW-STORJ", "KRW-GRS", "KRW-REP", "KRW-ADA", "KRW-SBD",
        "KRW-POWR", "KRW-BTG", "KRW-ICX", "KRW-EOS", "KRW-TRX",
        "KRW-SC", "KRW-ONT", "KRW-ZIL", "KRW-POLYX", "KRW-ZRX",
        "KRW-LOOM", "KRW-BCH", "KRW-BAT", "KRW-IOST", "KRW-RFR",
        "KRW-CVC", "KRW-IQ", "KRW-IOTA", "KRW-HIFI", "KRW-ONG",
        "KRW-GAS", "KRW-UPP", "KRW-ELF", "KRW-KNC", "KRW-BSV",
        "KRW-THETA", "KRW-QKC", "KRW-BTT", "KRW-MOC", "KRW-ENJ"
    ]
    prices = get_current_prices(tickers)
    return JsonResponse({'prices': prices})

def get(self, request):
    user = TradeList.objects.all()
    return render(request, 'JOCoin/test.html',context=dict(user = user))
    

def trade_coin(request):
    context = {}
    trade = CoinList.objects.filter()
    context[trade] = trade
    return render(request, "test.html",context)




    
    