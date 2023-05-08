# holding/
# 1. 실시간 코인별 수익률 계산 함수
def Per_return(rt_price, wallet_aver_price):
    return round(((rt_price - wallet_aver_price) / wallet_aver_price) * 100, 2)

# 2. 실시간 총 수익률 계산 함수
def Total_Per_return(total_cur, total_invest):
    return round((total_cur / total_invest)*100 ,2)