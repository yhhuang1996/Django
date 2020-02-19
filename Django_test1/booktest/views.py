from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from booktest.models import BookInfo, AreaInfo



# def my_render(template_path, context_dict={}):
#     # 1. 使用模板文件，返回模板对象
#     temp = loader.get_template(template_path)
#     # 2. 定义模板上下文：给模板文件传递数据
#     context = context_dict
#     # 3. 模板渲染：产生标准html内容
#     res_html = temp.render(context)
#     # 4. 返回给浏览器
#     return HttpResponse(res_html)


# Create your views here.
def index(request):
    # return HttpResponse('OK')
    book = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'book': book})


def create(request):
    new_book = BookInfo()
    new_book.btitle = '流星蝴蝶剑'
    new_book.bpub_date = date(1990, 1, 1)
    new_book.save()
    return redirect('/index')


def delete(request, bid):
    delete_book = BookInfo.objects.get(id=bid)
    delete_book.delete()
    return redirect('/index')


def detail(request, bid):
    # 查询bid对应图书信息
    book = BookInfo.objects.get(id=bid)
    # 查询图书对应英雄信息，一对多
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book': book, 'hero': heros})


def areas(request):
    area = AreaInfo.objects.get(aTitle='青岛市')
    parent = area.aParent
    children = area.areainfo_set.all()
    return render(request, 'booktest/areas.html', {'area': area, 'parent': parent, 'children': children})