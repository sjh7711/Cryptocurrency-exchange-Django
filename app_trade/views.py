from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from app_trade.models import *

import pyupbit

# Create your views here.


@login_required
@csrf_exempt
def trade(request):

    # 실시간 정보(Page-Column3)
    tickers = pyupbit.get_tickers(fiat= "KRW")
    prices = pyupbit.get_current_price(tickers)

    #########################################################################
    # 코인 이름 : coinList.coin_id 에서 값 가져온 값을 format을 사용하여 넣어줌 | 코인가격 : 코인이름(value값)을 사용하여 
    coin_data = CoinList.objects.values().exclude(coin_pk=0)
    coin_list = []

    for i in range(0, len(coin_data)):
        coin_dict = {}
        coin_dict["coin_name"] = coin_data[i]["coin_id"]
        coin_dict["coin_price"] = prices["{}".format(coin_data[i]["coin_id"])]
        coin_list.append(coin_dict)

    """   ############################################################################
    #호가창 매수,매도 (row들을 가져옴)
    order_buy_type = TradeList.objects.values().filter(coin_pk=15, tlog_cont_type = "매수", tlog_cont_time=None) 
    order_sell_type = TradeList.objects.values().filter(coin_pk=15,tlog_cont_type = "매도", tlog_cont_time=None)
    #############################################################################
    # 주문타입 : 매수 | 가격 : 매수가격 => sorted_type_buy_list 리스트에 딕셔너리 값 넣어줌
    type_is_buy_list = []
    for i in range(0, len(order_buy_type)):
        type_is_buy_dict = {}
        # i 번째의 row에서"tlog_cont_type"의 values를 가져옴
        type_is_buy_dict["coin_type"] = order_buy_type[i]["tlog_cont_type"]
        type_is_buy_dict["type_price"] = order_buy_type[i]["tlog_trade_price"]
        type_is_buy_list.append(type_is_buy_dict)
    # 낮을 숫자부터 정렬
    sorted_type_buy_list = sorted(type_is_buy_list)
    #############################################################################
    # 주문타입 : 매도 | 가격 : 매도가격 => type_is_sell_list 리스트에 딕셔너리 값 넣어줌
    type_is_sell_list = []
    for i in range(0,len(order_sell_type)):
        type_is_sell_dict = {}
        type_is_sell_dict["coin_type"] = order_sell_type[i]["tlog_cont_type"]
        type_is_sell_dict["type_price"] = order_sell_type[i]["tlog_trade_price"]
        type_is_sell_list.append(type_is_sell_dict)

    sorted_type_sell_list = sorted(type_is_sell_list)
    ###############################################################################
    # 주문타입 = 매수 | 가격 = 매수가격                     
    for index in range(0,len(sorted_type_buy_list)): 
        if sorted_type_buy_list[index] < prices["KRW-ARK"]:
            continue
        else:
            order_list_updown = sorted_type_buy_list[index:(index-5)] #  실시간 가격보다 큰 5개의 ARK의 실시간 가격을 가져옴  
            break  
    if order_list_updown != 5:
        for index in range(len(order_list_updown)):
            if order_list_updown[index] < prices["KRW-ARK"]:
                pre_index = index
            else:
                break


            
    ################################################################################
    # 주문타입 = 매도 | 가격 = 매도가격
    for index in range(len(sorted_type_sell_list)):
        if sorted_type_sell_list[index] < prices["KRW-ARK"]:
            continue
        else:
            order_list_updown = sorted_type_sell_list[(index+5):index]  
            break
    if order_list_updown != 5:
        for index in range(len(order_list_updown)):
            if order_list_updown[index] < prices["KRW-ARK"]:
                continue
            else:
                post_index = (10 - pre_index + len(order_list_updown))
                break
    for index in range(0,pre_index):
        order_list_updown.insert(index,"-")
    for index in range(0,post_index):
        order_list_updown.append("-") """
        
    

    ###########################################################################    
    # 미체결 총 거래량 
    # order_amnt = {}
    # for order_price_values in order_list_updown_price:
    #     if order_price_values in sorted_type_buy_list:
    #         order_amnt[order_price_values] +=1
    #     else:
    #         order_amnt[order_price_values] = 1
    ###########################################################################      
    # order_list_buy = []
    # order_list_sell = []

    
        # order_dict_buy = {}
        # order_dict_sell = {}

        # if data["tlog_cont_type"] == "매도":
        #     order_dict_sell["trade_price"] = data["tlog_trade_price"]
        #     order_dict_buy["trade_type"] = data["tlog_cont_type"]

        # elif data["tlog_cont_type"] == "매수":
        #     order_dict
    ##################################################################################
    # 호가창 정보 (Page-Column1)
    """    order_data = TradeList.objects.values().filter(coin_pk = 15,tlog_cont_time = None) 
    order_list = [] 
    for data in order_data:
        save_data = data["tlog_trade_price"]
        order_list.append(save_data)
    sorted_order_data = sorted(order_list) """


    # for index in range(0,len(sorted_order_data)):
    #     if sorted_order_data[index] < prices["KRW-ARK"]:
    #         continue
    #     else:
    #         order_list_updown = sorted_order_data[(index-5):(index+5)]
    #         break
    
    
    # if len(order_list_updown) != 10:
    #     for index in range(0,len(order_list_updown)):
    #         if order_list_updown[index] < prices["KRW-ARK"]:
    #             continue
    #         else:
    #             pre_index = 5 - index
    #             break
    

    # post_index = 10 - (pre_index + len(order_list_updown))

    # for index in range(0, pre_index):
    #     order_list_updown.insert(index, '-')

    # for index in range(0,post_index):
    #     order_list_updown.append('-')
    

    # for data in order_list_updown:
    #     prices["KRW-ARK"]
    # order_list_updown = [ {"거래타입":"매도", "가격":"-" },{"거래타입":"매도", "가격":"-" }, {"거래타입":"매도", "가격":"-" },
    #                      {"거래타입":"매수", "가격":"-" }, ...]

    

    return render(request, "trade.html", {"coin_list":coin_list})
    # return JsonResponse({'tickers':prices})

# def trade(request):
#     tickers = pyupbit.get_tickers(fiat="KRW")
#     prices = pyupbit.get_current_price(tickers)
#     competition_data = TradeList.objects.values().filter(coin_pk = 15,tlog_cont_time = None) 
#     # data = competition_data[0]["tlog_trade_price"]
    
#     list_data = []
#     list_data = sorted(list_data)

#     for i in competition_data:
#         save_data = i["tlog_trade_price"]
#         list_data.append(save_data)
        
#         """ for{
#             여기만 돌려주는데
#         }
        
#         for:
#             "여기까지가 } """

#     for index in range(0,len(list_data)):
#         if list_data[index] < prices["KRW-ARK"]:
#             continue
#         else:
#             list_data = list_data[(index-5):(index+5)]
#             break
    
#     if len(list_data) != 10:
#         for index in range(0,len(list_data)):
#             if list_data[index] < prices["KRW-ARK"]:
#                 continue
#             else:
#                 pre_index = 5 - index
#                 break

#     post_index = 10 - (pre_index + len(list_data))

#     for index in range(0, pre_index):
#         list_data.insert(index, '-')

#     for index in range(0,post_index):
#         list_data.append('-')
                

#     return render(request, 'trade.html',({"tickers":tickers, "prices":prices, "list_data":list_data}))



@login_required
@csrf_exempt
def submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # 양식으로부터 제출된 데이터를 처리하는 코드 작성
        # return HttpResponse("제출된 데이터: 이름={}, 이메일={}, 비밀번호={}".format(name, email, password))
    