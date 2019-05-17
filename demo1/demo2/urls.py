from django.conf.urls import url
# 引入 视图函数里面的所有类和 函数
from .views import *
# urlpatterns  格式要求 必须填写

app_name='demo2'

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^booklist/$',booklist,name='booklist'),
    url(r'^role/(\d+)/$',role,name='role'),

]