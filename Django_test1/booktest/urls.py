from django.urls import path, re_path
from booktest import views


urlpatterns = [
    path('index/', views.index),
    path('create/', views.create),
    path('areas/', views.areas),
    re_path(r'delete/(\d+)/$', views.delete),
    re_path(r'^books/(\d+)/$', views.detail),
    path('show_args<int:num>/', views.show_arg),
    path('login/', views.login),
    path('ajax_test/', views.ajax),
    path('ajax_handle/', views.ajax_handle),
    path('ajax_login/', views.ajax_login),
    path('ajax_check/', views.ajax_check),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('set_session/', views.set_session),
    path('get_session/', views.get_session),
]