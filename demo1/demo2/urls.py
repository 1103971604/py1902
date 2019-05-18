from django.conf.urls import url
# 引入 视图函数里面的所有类和 函数
from .views import *
# urlpatterns  格式要求 必须填写

app_name='demo2'

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^booklist/$',booklist,name='booklist'),
    url(r'^role/(\d+)/$',role,name='role'),
    url(r'^delbook/(\d+)/$',delbook,name='delbook'),
    url(r'^delrole/(\d+)/$',delrole,name='delrole'),
    url(r'^addbook/$',addbook,name='addbook'),
    url(r'^addrole/(\d+)/$',addrole,name='addrole'),
    url(r'^setbook/(\d+)/$',setbook,name='setbook'),
    url(r'^setrole/(\d+)/$',setrole,name='setrole'),
    # url(r'^/$'),


]