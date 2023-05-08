from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class CoinList(models.Model):
    coin_pk = models.AutoField(primary_key=True)
    coin_id = models.CharField(max_length=20)
    coin_amnt = models.BigIntegerField()
    coin_last_value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'coin_list'
        
class TradeList(models.Model):
    trade_pk = models.BigAutoField(primary_key=True)  
    # The composite primary key (trade_pk, user_pk, coin_pk) found, that is not supported. The first column is selected.
    user_pk = models.IntegerField()
    coin_pk = models.IntegerField()
    tlog_cont_time = models.FloatField(blank=True, null=True)
    tlog_cont_type = models.CharField(max_length=2)
    tlog_coin_amnt = models.BigIntegerField()
    tlog_trade_price = models.IntegerField()
    tlog_total_price = models.BigIntegerField()
    tlog_charge = models.IntegerField()
    tlog_earn_rate = models.IntegerField(blank=True, null=True)
    tlog_order_time = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trade_list'
        unique_together = (('trade_pk', 'user_pk', 'coin_pk'),)


class UserList(models.Model):
    user_pk = models.AutoField(primary_key=True)  # The composite primary key (user_pk, user_id) found, that is not supported. The first column is selected.
    user_id = models.CharField(max_length=40)
    user_pw = models.CharField(max_length=128)
    user_pn = models.CharField(max_length=40)
    user_em = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user_list'
        unique_together = (('user_pk', 'user_id'),)


class WalletList(models.Model):
    user_pk = models.IntegerField(primary_key=True)  # The composite primary key (user_pk, coin_pk) found, that is not supported. The first column is selected.
    coin_pk = models.IntegerField()
    wallet_addr = models.CharField(max_length=128)
    wallet_coin_amnt = models.BigIntegerField()
    wallet_aver_price = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wallet_list'
        unique_together = (('user_pk', 'coin_pk'),)