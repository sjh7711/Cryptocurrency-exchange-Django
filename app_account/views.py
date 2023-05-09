from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from app_account.models import *
from app_account.module import module

import pyupbit

# Create your views here.


# 입/출금 페이지
@login_required
@csrf_exempt
def account(request):
    info_user_pk=auth.get_user(request).id

    # krw_wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk))
    krw_wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk=0)
    krw_trade_data = TradeList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk=0)
    krw_log_list = []
    # j = 0 

    if not krw_wallet_data.exists() or krw_wallet_data[0]["wallet_addr"] is None:

    # if krw_wallet_data[0]["wallet_addr"] == '0':
        return render(request, "before_account.html")
    
    else:
        for i in range(0, len(krw_trade_data)):
            krw_log_dict = {}
            # 1. 입금/출금
            krw_log_dict["cont_type"] = krw_trade_data[i]["tlog_cont_type"]

            # 2. 입금/출금 시간
            krw_log_dict["cont_time"] = module.UtoD(krw_trade_data[i]["tlog_cont_time"])

            # 3. 입금/출금액
            krw_log_dict["total_price"] = krw_trade_data[i]["tlog_total_price"]
            krw_log_list.append(krw_log_dict)
        return render(request, "after_account.html", {"krw_log_list":krw_log_list})

    """ # 계좌 개설 전 페이지
    for i in range(0, len(krw_wallet_data)):
        check_coin_pk = krw_wallet_data[i]["coin_pk"]
        if check_coin_pk != 0:
            continue
        else:
            krw_trade_data = TradeList.objects.values().filter(user_pk='{}'.format(info_user_pk), coin_pk='{}'.format(i))
            krw_log_dict = {}
            # 1. 입금/출금
            krw_log_dict["cont_type"] = krw_trade_data[i]["tlog_cont_type"]

            # 2. 입금/출금 시간
            krw_log_dict["cont_time"] = krw_trade_data[i]["tlog_cont_type"]

            # 3. 입금/출금액
            krw_log_dict["total_price"] = krw_trade_data[i]["tlog_total_price"]
            krw_log_list.append(krw_log_dict)

            j = 1

            return render(request, "after_account.html", {"krw_log_list":krw_log_list})
    
    if j == 0 :
        phrase = {}
        return render(request, "before_account.html", {"phrase":phrase}) """
    

# tradelog/
# unixtime to datetime
from datetime import datetime
from time import time
    
nowtime = time()

# 계좌 생성 시, 주소 생성 및 1억 입금
@login_required
@csrf_exempt
def Cong(request):
    info_user_pk=auth.get_user(request).id
    # krw_wallet_data = WalletList(user_pk='{}'.format(info_user_pk), coin_pk=0, \
    #                                 wallet_addr='KRW', wallet_coin_amnt=10000000, wallet_aver_price=1)
    # krw_wallet_data.save()
    WalletList.objects.create(user_pk='{}'.format(info_user_pk), coin_pk=0, \
                                    wallet_addr='KRW', wallet_coin_amnt=10000000, wallet_aver_price=1)

    # krw_trade_data = TradeList(user_pk='{}'.format(info_user_pk), coin_pk=0,tlog_cont_time=time(), tlog_cont_type='입금',\
    #                             tlog_coin_amnt=100000000, tlog_trade_price=1, tlog_total_price=100000000, tlog_charge=0,\
    #                             tlog_earn_rate=0, tlog_order_time=time())
    # krw_trade_data.save()

    TradeList.objects.create(user_pk='{}'.format(info_user_pk), coin_pk=0,tlog_cont_time=time(), tlog_cont_type='입금',\
                                tlog_coin_amnt=100000000, tlog_trade_price=1, tlog_total_price=100000000, tlog_charge=0,\
                                tlog_earn_rate=0, tlog_order_time=time())

    # wallet_insert = WalletList(user_pk='{}'.format(info_user_pk), coin_pk=1, wallet_addr='0', wallet_coin_amnt=0, wallet_aver_price=0)
    # wallet_insert.save()

    coin_data = CoinList.objects.values().exclude(coin_pk=0)

    for i in range(0, len(coin_data)):
        WalletList.objects.create(user_pk='{}'.format(info_user_pk), coin_pk='{}'.format(coin_data[i]["coin_pk"]),\
                                   wallet_addr='0', wallet_coin_amnt=0, wallet_aver_price=0)
        # wallet_insert = WalletList(user_pk='{}'.format(info_user_pk), coin_pk='{}'.format(coin_data[i]["coin_pk"]),\
        #                            wallet_addr='0', wallet_coin_amnt=0, wallet_aver_price=0)
        # wallet_insert.save()

    return render(request, "Cong.html")

