from django.db import models
# 设计和表对应的类，模型类
# Create your models here.



class BookInfo(models.Model):
    """图书模型类，一类"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄人物类，多类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey(BookInfo, models.CASCADE)
    isDelete = models.BooleanField(default=False)

