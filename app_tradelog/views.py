from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from app_tradelog.models import *
from app_tradelog.module import module

import pyupbit

# Create your views here.

# 거래내역 페이지
@login_required
@csrf_exempt
def tradelog(request):
    info_user_pk=auth.get_user(request).id
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
        if trade_data[i]["tlog_cont_time"] is None:
            log_dict["cont_time"] = '-'
        else:
            log_dict["cont_time"] = module.UtoD(trade_data[i]["tlog_cont_time"]/10000)
            
        # 2. 주문시간
        log_dict["order_time"] = module.UtoD(trade_data[i]["tlog_order_time"]/10000)
        # 4. 매수/매도
        log_dict["cont_type"] = trade_data[i]["tlog_cont_type"]
        # 5. 코인량
        log_dict["coin_amnt"] = trade_data[i]["tlog_coin_amnt"] / 10000
        # 6. 거래단가
        log_dict["trade_price"] = trade_data[i]["tlog_trade_price"] /10000
        # 7. 총금액
        log_dict["total_price"] = trade_data[i]["tlog_total_price"] / 100000000

        log_list.append(log_dict)

    return render(request, "tradelog.html", {"log_list":log_list})