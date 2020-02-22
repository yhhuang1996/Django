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


def login_require(view_func):
    """登录判断装饰器"""
    def wrapper(request, *args, **kwargs):
        """判断用户是否登录"""
        if 'has_login' in request.session:
            # 用户已登陆，调用对应的视图
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrapper


def login(request):
    if 'has_login' in request.session:
        return redirect('/change_password')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    # request.POST  保存的是POST方式提交的参数
    # request.GET  保存的是GET方式提交的参数
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到首页
        # response = redirect('/index')
        response = redirect('/change_password')
        if remember == 'on':
            response.set_cookie('username', username)
        request.session['has_login'] = True
        request.session['username'] = username
        return response
    else:
        # 用户名密码错误，跳转到登录页面
        return redirect('/login')
    # 2.验证
    # 3.返回应答
    # return HttpResponse('ok')


@login_require
def change_password(request):
    return render(request, 'booktest/change_password.html')


@login_require
def change_check(request):
    new_password = request.POST.get('password')
    check = request.POST.get('check_password')
    username = request.session['username']
    if new_password == check:
        return HttpResponse('%s 修改密码为：%s' % (username, check))
    else:
        return redirect('/change_password')


def ajax(request):
    return render(request, 'booktest/ajax_test.html')


def ajax_handle(request):
    return JsonResponse({'res': 1})


def ajax_login(request):
    # 判断用户是否登录
    if 'is_login' in request.session:
        # 用户已登录，跳转到首页
        return redirect('/index')
    else:
        # 获取cookie username
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
            print(username)
        else:
            username = ''
        return render(request, 'booktest/ajax_login.html', {'username': username})


def ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(remember)
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到首页
        ret = 1
        # 记住用户登录状态
        request.session['is_login'] = True
        if remember == 'on':
            response = JsonResponse({'res': ret})
            response.set_cookie('username', username, max_age=24 * 3600)
            return response
    else:
        # 用户名密码错误，跳转到登录页面
        ret = 0
    return JsonResponse({'res': ret})


def set_cookie(request):
    response = HttpResponse()
    # response.set_cookie('num', 1)
    response.set_cookie('num', 1, max_age=14 * 24 * 3600)
    return response


def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)


def set_session(request):
    request.session['username'] = 'smart'
    request.session['age'] = 18
    return HttpResponse('设置session')


def get_session(request):
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + str(age))


def temp_var(request):
    my_dict = {'title': '值'}
    my_list = [1, 2, 3]
    book = BookInfo.objects.get(id=1)
    context = {'my_dict': my_dict, 'my_list': my_list, 'book': book}
    return render(request, 'booktest/temp_var.html', context)


def temp_tags(request):
    book = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {'book': book})


def temp_filter(request):
    book = BookInfo.objects.all()
    return render(request, 'booktest/temp_filter.html', {'book': book})


def temp_inherit(request):
    """模版继承"""
    return render(request, 'booktest/child.html')


def html_escape(request):
    return render(request, 'booktest/html_escape.html', {'content': '<h1>hello</h1>'})


def url_reverse(request):
    return render(request, 'booktest/url_reverse.html')


def show_args(request, a):
    return HttpResponse('ok')


from django.urls import reverse
def test_redirect(request):
    url = reverse('booktest:args', kwargs={'a': 2})
    return redirect(url)