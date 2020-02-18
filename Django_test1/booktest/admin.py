from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    """英雄模型管理类"""
    list_display = ['id', 'hname', 'hcomment', 'hbook']

# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

