# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class CoinList(models.Model):
    coin_pk = models.AutoField(primary_key=True)
    coin_id = models.CharField(max_length=20)
    coin_amnt = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'coin_list'


class NewAccount(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'new_account'


class TradeList(models.Model):
    user_pk = models.CharField(primary_key=True, max_length=8)  # The composite primary key (user_pk, coin_pk) found, that is not supported. The first column is selected.
    coin_pk = models.CharField(max_length=8)
    tlog_cont_time = models.IntegerField(blank=True, null=True)
    tlog_cont_type = models.CharField(max_length=2)
    tlog_coin_amnt = models.BigIntegerField()
    tlog_trade_price = models.IntegerField()
    tlog_total_price = models.BigIntegerField()
    tlog_charge = models.IntegerField()
    tlog_earn_rate = models.IntegerField(blank=True, null=True)
    tlog_order_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trade_list'
        unique_together = (('user_pk', 'coin_pk'),)


class UserList(models.Model):
    user_pk = models.AutoField(primary_key=True)
    user_id = models.CharField('', max_length=40)
    user_pw = models.CharField('', max_length=40)
    user_pn = models.CharField('', max_length=40)
    user_em = models.CharField('', max_length=40)

    class Meta:
        managed = False
        db_table = 'user_list'


class WalletList(models.Model):
    user_pk = models.CharField(primary_key=True, max_length=8)  # The composite primary key (user_pk, coin_pk) found, that is not supported. The first column is selected.
    coin_pk = models.CharField(max_length=8)
    wallet_addr = models.CharField(max_length=16)
    wallet_coin_amnt = models.BigIntegerField()
    wallet_aver_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wallet_list'
        unique_together = (('user_pk', 'coin_pk'),)
