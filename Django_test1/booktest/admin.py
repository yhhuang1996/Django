from django.contrib import admin
from booktest.models import BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    """图书模型管理类"""
    list_display = ['id', 'btitle', 'bpub_date']

# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)

