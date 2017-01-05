from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.
def cart(request):
    li={'t':'购物车'}
    con={'tt':li}
    return render(request,'cartPage/cart.html',con)
def order(request):
    li = {'t': '提交订单'}
    con = {'tt': li}
    return render(request,'cartPage/order.html',con)
