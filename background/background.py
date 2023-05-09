import schedule
import time

def contract():
    noCtract = TradeList.objects.filter(tlog_cont_time=None)
    coins = CoinList.objects.all()
    wallets = WalletList.objects.all()
    nowPrice = pyupbit.get_current_price(list(map(lambda x:x.coin_id, coins)))
    coinIds = list(map(lambda x:x.coin_id, coins))
    
    for i in noCtract:
        if i.tlog_cont_type == "매수" and i.tlog_trade_price >= nowPrice[coinIds[i.coin_pk]]:
            i.tlog_cont_time = time.time()
            i.save()
        if i.tlog_cont_type == "매도" and i.tlog_trade_price <= nowPrice[coinIds[i.coin_pk]]:
            i.tlog_cont_time = time.time()
            i.tlog_earn_rate = round(nowPrice[coinIds[i.coin_pk]]/(WalletList.objects.filter(coin_pk=i.coin_pk, user_pk=i.user_pk)[0].wallet_aver_price),4)*10000
            i.save()
            
# def update():
#     noCtract = TradeList.objects.filter(tlog_cont_time=None)
#     coins = CoinList.objects.all()
#     wallets = WalletList.objects.all()
#     nowPrice = pyupbit.get_current_price(list(map(lambda x:x.coin_id, coins)))
#     coinIds = list(map(lambda x:x.coin_id, coins))
    
#     for i in noCtract:
#         if i.tlog_cont_type == "매수" and i.tlog_trade_price >= nowPrice[coinIds[i.coin_pk]]:
#             i.tlog_cont_time = time.time()
#             i.save()
#         if i.tlog_cont_type == "매도" and i.tlog_trade_price <= nowPrice[coinIds[i.coin_pk]]:
#             i.tlog_cont_time = time.time()
#             i.tlog_earn_rate = round(nowPrice[coinIds[i.coin_pk]]/(WalletList.objects.filter(coin_pk=i.coin_pk, user_pk=i.user_pk)[0].wallet_aver_price),4)*10000
#             i.save()
            
while True:
    views.contract()
    print(1)
    time.sleep(1)