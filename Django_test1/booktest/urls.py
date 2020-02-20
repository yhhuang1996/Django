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
    path('login_check/', views.login_check)
]