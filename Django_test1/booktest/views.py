from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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


def show_arg(request, num):
    return HttpResponse(num)


def login(request):
    return render(request, 'booktest/login.html')


def login_check(request):
    # request.POST  保存的是POST方式提交的参数
    # request.GET  保存的是GET方式提交的参数
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到首页
        return redirect('/index')
    else:
        # 用户名密码错误，跳转到登录页面
        return redirect('/login')
    # 2.验证
    # 3.返回应答
    # return HttpResponse('ok')


def ajax(requset):
    return render(requset, 'booktest/ajax_test.html')


def ajax_handle(request):
    return JsonResponse({'res': 1})


def ajax_login(requset):
    return render(requset, 'booktest/ajax_login.html')


def ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到首页
        ret = 1
    else:
        # 用户名密码错误，跳转到登录页面
        ret = 0
    return JsonResponse({'res': ret})
