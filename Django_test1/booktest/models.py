from django.db import models
# 设计和表对应的类，模型类
# Create your models here.


class BookInfoManager(models.Manager):
    """图书模型管理器类"""
    pass


class BookInfo(models.Model):
    """图书模型类，一类"""
    # btitle = models.CharField(max_length=20)
    btitle = models.CharField(max_length=20, unique=True)  # 图书名唯一
    bprice = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # bpub_date = models.TimeField()  #  时分秒
    # bpub_date = models.DateField()  #  日期
    # bpub_date = models.DateTimeField()  # 年月日时分秒
    # bpub_date = models.DateField(auto_now_add=True)  # 创建时间
    bpub_date = models.DateField(auto_now=True)  # 修改时间
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    object = BookInfoManager()

class HeroInfo(models.Model):
    """英雄人物类，多类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey(BookInfo, models.CASCADE)
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    aTitle = models.CharField(max_length=20)
    # aProvince = models.CharField(max_length=20)
    # aCity = models.CharField(max_length=20)
    # aDistrict = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
