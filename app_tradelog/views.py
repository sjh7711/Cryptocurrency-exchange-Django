from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from app_tradelog.module import module

import pyupbit

# Create your views here.

# 거래내역 페이지
@csrf_exempt
def tradelog(request):
    info_user_pk=1
    trade_data = TradeList.objects.values().filter(user_pk='{}'.format(info_user_pk)).exclude(coin_pk=0)
    coin_data = CoinList.objects.values().exclude(coin_pk=0)

    log_list = []

    for i in range(0, len(trade_data)):
        log_dict = {}
        log_coin_pk = trade_data[i]["coin_pk"]

        for j in range(0, len(coin_data)):
            coin_coin_pk = coin_data[j]["coin_pk"]
            if log_coin_pk == coin_coin_pk:
                # 3. 코인명
                log_dict["coin_name"] = coin_data[j]["coin_id"][4:]
                     
        # 1. 체결시간
        if trade_data[i]["tlog_cont_time"] is not None:
            log_dict["cont_time"] = module.UtoD(trade_data[i]["tlog_cont_time"])
        else:
            log_dict["cont_time"] = '-'
        # 2. 주문시간
        log_dict["order_time"] = module.UtoD(trade_data[i]["tlog_order_time"])
        # 4. 매수/매도
        log_dict["cont_type"] = trade_data[i]["tlog_cont_type"]
        # 5. 코인량
        log_dict["coin_amnt"] = trade_data[i]["tlog_coin_amnt"]
        # 6. 거래단가
        log_dict["trade_price"] = trade_data[i]["tlog_trade_price"]
        # 7. 총금액
        log_dict["total_price"] = trade_data[i]["tlog_total_price"]

        log_list.append(log_dict)

    return render(request, "tradelog.html", {"log_list":log_list})