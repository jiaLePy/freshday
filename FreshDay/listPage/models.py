from django.db import models

# Create your models here.


class TypeInfo(models.Model):
    title = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gtype = models.ForeignKey('TypeInfo')
    gprice = models.DecimalField(max_digits=8, decimal_places=2)
    gdesc = models.CharField(max_length=1000)
    gpic=models.ImageField(upload_to='goods/')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gtitle.encode('utf-8')
