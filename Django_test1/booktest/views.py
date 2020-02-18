from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from booktest.models import BookInfo
from booktest.models import HeroInfo


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
    return render(request, 'booktest/index.html', {'content': 'hello world', 'list': list(range(1, 9))})


def books(request):
    b = BookInfo.objects.all()
    return render(request, 'booktest/books.html', {'book_name': b})


def detail(request, bid):
    # 查询bid对应图书信息
    book = BookInfo.objects.get(id=bid)
    # 查询图书对应英雄信息，一对多
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book': book, 'hero': heros})