from django.urls import path, re_path
from booktest import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<int:a>', views.show_args, name='args'),
    path('test_redirect/', views.test_redirect),
    path('create/', views.create),
    path('areas/', views.areas),
    re_path(r'delete/(\d+)/$', views.delete),
    re_path(r'^books/(\d+)/$', views.detail),
    path('show_args<int:num>/', views.show_arg),
    path('login/', views.login),
    path('login_check/', views.login_check),
    path('change_password/', views.change_password),
    path('change_check/', views.change_check),
    path('ajax_test/', views.ajax),
    path('ajax_handle/', views.ajax_handle),
    path('ajax_login/', views.ajax_login),
    path('ajax_check/', views.ajax_check),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session),
    path('temp_var/', views.temp_var),
    path('temp_tags/', views.temp_tags),
    path('temp_filter/', views.temp_filter),
    path('temp_inherit/', views.temp_inherit),
    path('html_escape/', views.html_escape),
    path('url_reverse/', views.url_reverse),
]