from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

class UserInfo(models.Model):
    uname = models.CharField(max_length=20, unique=True)
    upwd = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    tel = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    email = models.CharField(max_length=40, unique=True)
    def hContent(self):
        return format_html(self.hcontent)

class TypeInfo(models.Model):
    title = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gtype = models.ForeignKey('TypeInfo')
    gprice = models.DecimalField(max_digits=8, decimal_places=2)
    gdesc = models.CharField(max_length=1000)
    gpic=models.ImageField(upload_to='goods/')
    isDelete = models.BooleanField(default=False)

class CartInfo(models.Model):
    cuser = models.ForeignKey('UserInfo')
    cgoods = models.ForeignKey('GoodsInfo')
    count = models.IntegerField(default=0)

class OrderInfo(models.Model):
    ouser = models.ForeignKey('UserInfo')
    ototal = models.DecimalField(max_digits=8, decimal_places=2)
    state = models.BooleanField(default=False)

class OrderDetailInfo(models.Model):
    order = models.ForeignKey('OrderInfo')
    goods = models.ForeignKey('GoodsInfo')
    count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class DestAddrInfo(models.Model):
    name=models.ForeignKey('UserInfo')
    addr=models.CharField(max_length=100)
    tel=models.IntegerField()
    postcode=models.IntegerField()








