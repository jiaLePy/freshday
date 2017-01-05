#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from models import *
# Create your views here.
def cart(request):
    #value=request.session.get('#session键名字')
    value=1
    if value == None:
        return redirect('/cartPage/loginTest/')
    else:

        login_user=UserInfo.objects.filter(uname='zhou')
        user_id=login_user[0].id      #登陆的用户名的id

        cart=CartInfo.objects.filter(cuser_id=user_id)  #当前用户要买的所有商品
        dic=[]
        for temp in cart:
            dic.append({'goods':temp.cgoods.gtitle,'count':temp.count,'price':temp.cgoods.gprice,'pic':temp.cgoods.gpic,'tprice':temp.count*temp.cgoods.gprice})
        li={'t':'购物车'}
        con={'tt':li,'t2':dic}
        return render(request,'cartPage/cart.html',con)
def order(request):
    li = {'t': '提交订单'}
    con = {'tt': li}
    return render(request,'cartPage/order.html',con)

def loginTest(request):
    return render(request,'cartPage/loginTest.html')
