from django.urls import path, re_path
from booktest import views


urlpatterns = [
    path('index/', views.index),
    path('books/', views.books),
    re_path(r'^books/(\d+)/$', views.detail),
]