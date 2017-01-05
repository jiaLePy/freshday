from django.shortcuts import render
from models import *
from django.core.paginator import Paginator

# Create your views here.
def list(request,pindex):
    list = GoodsInfo.objects.all()
    page = Paginator(list, 10)
    if pindex == '':
        pindex = '1'
    pindex = int(pindex)
    list2 = page(pindex)
    plist = page.page_range
    context = {'list':list,'lisT':list2,'plist':plist,'pindex':pindex}

    return render(request,'list.html',context)

def page(request,pindex):
    list = GoodsInfo.objects.all()
    page = Paginator(list,10)
    if pindex =='':
        pindex = '1'
    pindex = int(pindex)
    list2 = page(pindex)
    plist = page.page_range
    render(request,'list.html',{'lisT':list2,'plist':plist,'pindex':pindex})


