# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='destAddrInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('addr', models.CharField(max_length=100)),
                ('tel', models.IntegerField()),
                ('postcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=8, decimal_places=2)),
                ('gdesc', models.CharField(max_length=1000)),
                ('gpic', models.ImageField(upload_to=b'goods/')),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('goods', models.ForeignKey(to='mainPage.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ototal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(unique=True, max_length=20)),
                ('upwd', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('email', models.CharField(unique=True, max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='ouser',
            field=models.ForeignKey(to='mainPage.UserInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='mainPage.OrderInfo'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='mainPage.TypeInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='cgoods',
            field=models.ForeignKey(to='mainPage.GoodsInfo'),
        ),
        migrations.AddField(
            model_name='cartinfo',
            name='cuser',
            field=models.ForeignKey(to='mainPage.UserInfo'),
        ),
    ]
