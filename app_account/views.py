from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_account.models import *

import pyupbit

# Create your views here.

# 입/출금 페이지
@csrf_exempt
def account(request):
    info_user_pk=1

    krw_wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk=0)
    krw_trade_data = TradeList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk=0)

    krw_log_list = []

    # 계좌 개설 전 페이지
    if krw_wallet_data[0]["wallet_addr"] is None:
        return render(request, "before_account.html")
    

    # 계좌 개설 후 페이지
    else:
        for i in range(0, len(krw_trade_data)):
            krw_log_dict = {}
            # 1. 입금/출금
            krw_log_dict["cont_type"] = krw_trade_data[i]["tlog_cont_type"]

            # 2. 입금/출금 시간
            krw_log_dict["cont_time"] = krw_trade_data[i]["tlog_cont_type"]

            # 3. 입금/출금액
            krw_log_dict["total_price"] = krw_trade_data[i]["tlog_total_price"]
            krw_log_list.append(krw_log_dict)
            
    return render(request, "after_account.html", {"krw_log_list":krw_log_list})

# 계좌 생성 시, 주소 생성 및 1억 입금
@csrf_exempt
def Cong(request):
    info_user_pk=1

    krw_wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk=0)
    krw_wallet_data.update(wallet_addr='KRW', wallet_coin_amnt=100000000, wallet_aver_price=1)

    return render(request, "after_account.html")
