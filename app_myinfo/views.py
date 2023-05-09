from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .models import CoinList, TradeList, UserList
from django.contrib import messages
import pyupbit
import time

@login_required
@csrf_exempt
def myinfo(request):
    return render(request, "myinfo.html")