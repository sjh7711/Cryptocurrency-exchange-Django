import time
import pyupbit 
import pymysql
import schedule

conn = pymysql.connect(host="144.24.88.224", user="root", password="Jonghwa123@", db="project", charset="utf8")
cur = conn.cursor()

def contract():
    cur.execute("SELECT * FROM trade_list WHERE tlog_cont_time is null")
    noCtract = cur.fetchall()

    cur.execute("SELECT * FROM coin_list")
    coins = cur.fetchall()
    nowPrice = pyupbit.get_current_price(list(map(lambda x:x[1],coins)))
    
    #i[0] : trade pk              #wallet[0] : user pk
    #i[1] : user pk               #wallet[1] : coin pk
    #i[2] : coin pk               #wallet[2] : 코인 주소
    #i[3] : 체결시간               #wallet[3] : 코인 양
    #i[4] : 체결타입               #wallet[4] : 코인 평균가
    #i[5] : 코인 양
    #i[6] : 코인 주문가
    #i[7] : 코인 양 * 주문가
    #i[8] : 수수료
    #i[9] : 수익률
    #i[10] : 주문 시간
    for i in noCtract:
        print( i[4],  i[6]/10000, nowPrice[coins[i[2]-1][1]])
        if i[4] == "매수" and i[6]/10000 >= nowPrice[coins[i[2]-1][1]]:
            print(1)
            cur.execute("SELECT * FROM wallet_list WHERE coin_pk = {val1} and user_pk = {val2}".format(val1=i[2], val2=i[1]))
            walletData = cur.fetchone()
            print(walletData)
            #wallet에서 구매한 coin으로 생기는 평균가 변동 측정을 위해 가져오는 정보
            ap = (walletData[4]*walletData[3] + nowPrice[coins[i[2]-1][1]]*i[5])/(walletData[3]+i[5]) #(wallet 평균가 * wallet 코인 개수 + 새로 살 떄 든 돈 ) / (지갑에 코인 양 + 주문한 코인 양)
            print(ap)
            #코인 평균가 계산
            cur.execute("UPDATE trade_list SET tlog_cont_time = {val0}, tlog_trade_price = {val1}, tlog_total_price = {val2} WHERE trade_pk = {val3}"\
                .format(val0=time.time()*10000, val1=nowPrice[coins[i[2]-1][1]]*10000, val2=nowPrice[coins[i[2]-1][1]]*i[5]*10000, val3=i[0]))
            #trade 테이블에 구메 체결된 정보 저장 ( 체결된 시간, 실거래 된 가격, 실 거래 총액 )
            cur.execute("UPDATE wallet_list SET wallet_coin_amnt = wallet_coin_amnt + {val0} , wallet_aver_price = {val}\
                WHERE coin_pk = {val2} and user_pk ={val3}".format(val0=i[5], val1=ap, val2=i[2], val3=i[1]))
            #wallet에서 평균가 및 코인 개수 변경 
            cur.execute("UPDATE wallet_list SET wallet_coin_amnt = wallet_coin_amnt - {val0} \
                WHERE coin_pk = 0 and user_pk = {val3}".format(val0=nowPrice[coins[i[2]-1][1]]*i[5], val3=i[1]))
            #wallet에서 원화 감소
            conn.commit()
        elif i[4] == "매도" and i[6]/10000 <= nowPrice[coins[i[2]-1][1]]:
            print(3)
            cur.execute("SELECT * FROM wallet_list WHERE coin_pk = {val1} and user_pk = {val2}".format(val1=i[2], val2=i[1]))
            walletData = cur.fetchone()
            print(walletData)
            cur.execute("UPDATE wallet_list SET wallet_coin_amnt = wallet_coin_amnt - {val0} WHERE coin_pk = {val1} and user_pk ={val2}".format(val0=i[5], val1=i[2], val2=i[1]))
            #wallet 에서 판매한 코인 개수 감소
            cur.execute("UPDATE wallet_list SET wallet_coin_amnt = wallet_coin_amnt + {val0} WHERE coin_pk = 0 and user_pk ={val2}".format(val0=(i[5]*coins[i[2]-1][1])/10000, val2=i[1]))
            #wallet 에서 원화 증가
            cur.execute("UPDATE trade_list SET tlog_cont_time = {val0}, tlog_trade_price = {val1}, tlog_total_price = {val2}, tlog_earn_rate = {val3} WHERE trade_pk = {val4}"\
                .format(val0=time.time()*10000,val1=nowPrice[coins[i[2]-1][1]]*10000, val2=nowPrice[coins[i[2]-1][1]]*i[5]*10000, val3=round((nowPrice[coins[i[2]-1][1]]*10000 - walletData[4])/(nowPrice[coins[i[2]-1][1]]*10000)*100,4)*10000, val4=i[0]))
            conn.commit()
    
def update():
    cur.execute("SELECT * FROM coin_list")
    coins = cur.fetchall()
    nowPrice = pyupbit.get_current_price(list(map(lambda x:x[1],coins)))
    
    for i in coins:
        cur.execute("UPDATE coin_list SET coin_last_value = {val1} WHERE coin_pk = {id}".format(val1=nowPrice[i[1]]*10000, id=i[0]))
    conn.commit()
    print(2)

schedule.every(1).seconds.do(contract)
schedule.every().day.at("09:00").do(update)

while True:
    schedule.run_pending()
    time.sleep(1)