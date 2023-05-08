from django.shortcuts import render
from .models import Pybo
from urllib.request import Request, urlopen
from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pyupbit

class index:
    def get_current_prices(self, ticker):
        tickers = pyupbit.get_tickers(fiat="KRW")
        price = pyupbit.get_current_price(tickers)
        return price

    def get_prices(request):
        tickers = [  "KRW-BTC", "KRW-ETH", "KRW-NEO", "KRW-MTL", "KRW-XRP",
                   "KRW-ETC", "KRW-SNT", "KRW-WAVES", "KRW-XEM", "KRW-QTUM",
                   "KRW-LSK","KRW-STEEM","KRW-XLM","KRW-ARDR","KRW-ARK",
                   "KRW-STORJ","KRW-GRS","KRW-REP","KRW-ADA","KRW-SBD",
                   "KRW-POWR","KRW-BTG","KRW-ICX","KRW-EOS","KRW-TRX",
                   "KRW-SC","KRW-ONT","KRW-ZIL","KRW-POLYX","KRW-ZRX",
                   "KRW-LOOM","KRW-BCH","KRW-BAT","KRW-IOST","KRW-RFR",
                   "KRW-CVC","KRW-IQ","KRW-IOTA","KRW-HIFI","KRW-ONG",
                   "KRW-GAS", "KRW-UPP", "KRW-ELF", "KRW-KNC", "KRW-BSV",
                   "KRW-THETA","KRW-QKC","KRW-BTT","KRW-MOC", "KRW-ENJ"
                    ]
        prices = []
        index_instance = index()
        prices = index_instance.get_current_prices(tickers)   
        return JsonResponse({'prices':prices})
    
    
class Main():
    def get(self, request):
        user = Pybo.objects.all()
        return render(request, 'main.html',context=dict(user = user))





    
    