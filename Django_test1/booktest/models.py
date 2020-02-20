from django.db import models
# 设计和表对应的类，模型类
# Create your models here.


class BookInfoManager(models.Manager):
    """图书模型管理器类"""
    # 1.改变查询结果集
    def all(self):
        # 1.调用父类的all方法,获取所有数据
        book = super().all()
        # 2.对数据进行过滤
        book.filter(isDelete=True)
        # 3.返回book
        return book

    # 2.添加额外方法，操作模型类对应的数据表
    def create_book(self, btitle, bpub_date):
        # 1.创建一个图书对象
        # 获取self所在的模型类
        book = self.model()

        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.保存进数据库
        book.save()
        # 3.返回obj
        return book


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

    objects = BookInfoManager()

    # 元选项
    # 指定模型类对应的表名
    class Meta:
        db_table = 'bookinfo'

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     # 1.创建一个图书对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 2.保存进数据库
    #     obj.save()
    #     # 3.返回obj
    #     return obj


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
