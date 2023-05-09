from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib import auth
from app_holding.models import *
from app_holding.module import Calc

import pyupbit

# Create your views here.

# 보유 자산 페이지
@login_required
@csrf_exempt
def holding(request):
    info_user_pk=auth.get_user(request).id

    # 코인 정보 조회
    tickers = pyupbit.get_tickers(fiat="KRW")
    nowPrice = pyupbit.get_current_price(tickers)

    # render the initial HTML template
    if request.method == 'GET':
        coin_data = CoinList.objects.values()
        wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk))

        # Setting
        holding_list_top = []
        holding_dict_top = {}
        total_buy_price=0
        total_eval_price=0

        holding_list_bot = []

        for i in range(0, len(wallet_data)):
            holding_dict_bot = {}

            if wallet_data[i]["coin_pk"] == 0:
                # 상단부 1. 보유 KRW
                holding_dict_top["holding_KRW"] = wallet_data[i]["wallet_coin_amnt"]
        
            else:
                holding_dict_bot = {}
                wallet_coin_pk = wallet_data[i]["coin_pk"]

                for j in range(0, len(coin_data)):
                    coin_coin_pk = coin_data[j]["coin_pk"]

                    if wallet_coin_pk == coin_coin_pk:
                        # 하단부 1. 코인명
                        holding_dict_bot["coin_name"] = coin_data[j]["coin_id"][4:]

                        # 하단부 5.평가금액
                        holding_dict_bot["eval_price"] = wallet_data[i]["wallet_coin_amnt"] * nowPrice["{}".format(coin_data[j]["coin_id"])]
                        total_eval_price += wallet_data[i]["wallet_coin_amnt"] * nowPrice["{}".format(coin_data[j]["coin_id"])] # 총 평가금액
                        # 하단부 6.수익률(%)
                        if wallet_data[i]["wallet_aver_price"] != 0:
                            holding_dict_bot["Per_return"] = Calc.Per_return(nowPrice["{}".format(coin_data[j]["coin_id"])]*10000, wallet_data[i]["wallet_aver_price"])
                        else:
                            holding_dict_bot["Per_return"] = 0

                
                # 하단부 2.보유수량 
                holding_dict_bot["wallet_coin_amnt"] = wallet_data[i]["wallet_coin_amnt"]
                # 하단부 3.매수평균가 
                holding_dict_bot["wallet_aver_price"] = wallet_data[i]["wallet_aver_price"] / 10000
                # 하단부 4.매수금액 
                holding_dict_bot["buy_price"] = wallet_data[i]["wallet_coin_amnt"] * (wallet_data[i]["wallet_aver_price"] /10000)
                total_buy_price += wallet_data[i]["wallet_coin_amnt"] * (wallet_data[i]["wallet_aver_price"] / 10000) # 총 매수 금액

                holding_list_bot.append(holding_dict_bot)
    
        # 상단부 2. 총 매수금액
        holding_dict_top["total_buy_price"] = round(total_buy_price, 2)

        # 상단부 3. 총 평가 금액
        holding_dict_top["total_eval_price"] = round(total_eval_price, 2)

        # 상단부 4. 총 평가손익
        holding_dict_top["total_return"] = round((total_eval_price - total_buy_price), 2)

        # 상단부 5. 총 수익률
        if total_eval_price != 0:
            holding_dict_top["total_Per_return"] = Calc.Total_Per_return((total_eval_price-total_buy_price) , total_eval_price)
        else:
            holding_dict_top["total_Per_return"] = 0

        holding_list_top.append(holding_dict_top)


        return render(request, "holding.html", {"holding_list_top":holding_list_top, "holding_list_bot":holding_list_bot})

    # process the AJAX request and return JSON response
    elif request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        coin_data = CoinList.objects.values()
        wallet_data = WalletList.objects.values().filter(user_pk='{}'.format(info_user_pk))

        # Setting
        holding_list_top = []
        holding_dict_top = {}
        total_buy_price=0
        total_eval_price=0

        holding_list_bot = []
        holding_dict_bot2 = {}


        for i in range(0, len(wallet_data)):
            holding_dict_bot = {}

            if wallet_data[i]["coin_pk"] == 0:
                # 상단부 1. 보유 KRW
                holding_dict_top["holding_KRW"] = wallet_data[i]["wallet_coin_amnt"]
        
            else:
                holding_dict_bot = {}
                wallet_coin_pk = wallet_data[i]["coin_pk"]

                for j in range(0, len(coin_data)):
                    coin_coin_pk = coin_data[j]["coin_pk"]

                    if wallet_coin_pk == coin_coin_pk:
                        # 하단부 1. 코인명
                        holding_dict_bot["coin_name"] = coin_data[j]["coin_id"][4:]

                        # 하단부 5.평가금액
                        holding_dict_bot["eval_price"] = wallet_data[i]["wallet_coin_amnt"] * nowPrice["{}".format(coin_data[j]["coin_id"])]
                        total_eval_price += wallet_data[i]["wallet_coin_amnt"] * nowPrice["{}".format(coin_data[j]["coin_id"])] # 총 평가금액
                        # 하단부 6.수익률(%)
                        if wallet_data[i]["wallet_aver_price"] != 0:
                            holding_dict_bot["Per_return"] = Calc.Per_return(nowPrice["{}".format(coin_data[j]["coin_id"])]*10000, wallet_data[i]["wallet_aver_price"])
                        else:
                            holding_dict_bot["Per_return"] = 0

                
                # 하단부 2.보유수량 
                holding_dict_bot["wallet_coin_amnt"] = wallet_data[i]["wallet_coin_amnt"]
                # 하단부 3.매수평균가 
                holding_dict_bot["wallet_aver_price"] = wallet_data[i]["wallet_aver_price"] / 10000
                # 하단부 4.매수금액 
                holding_dict_bot["buy_price"] = wallet_data[i]["wallet_coin_amnt"] * (wallet_data[i]["wallet_aver_price"] /10000)
                total_buy_price += wallet_data[i]["wallet_coin_amnt"] * (wallet_data[i]["wallet_aver_price"] / 10000) # 총 매수 금액

                holding_dict_bot2["{}".format(wallet_coin_pk)] = holding_dict_bot
    
        # 상단부 2. 총 매수금액
        holding_dict_top["total_buy_price"] = round(total_buy_price, 2)

        # 상단부 3. 총 평가 금액
        holding_dict_top["total_eval_price"] = round(total_eval_price, 2)

        # 상단부 4. 총 평가손익
        holding_dict_top["total_return"] = round((total_eval_price - total_buy_price), 2)

        # 상단부 5. 총 수익률
        if total_eval_price != 0:
            holding_dict_top["total_Per_return"] = Calc.Total_Per_return((total_eval_price-total_buy_price) , total_eval_price)
        else:
            holding_dict_top["total_Per_return"] = 0

        holding_list_top.append(holding_dict_top)

        data = {
            "holding_dict_top":holding_dict_top,
            "holding_dict_bot2":holding_dict_bot2
        }

        return JsonResponse(data)
