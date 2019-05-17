from django.contrib import admin
from .models import bookinfo,roleinfo

class bookinfostyle(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ['title','put_time']
    #过滤字段
    list_filter = ['title','put_time']
    # 可以根据什么 查询数据
    search_fields = ['title','put_time']

class roleinfostyle(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ['name','sex','age']
    #过滤字段
    list_filter = ['name','sex','age']
    # 可以根据什么 查询数据
    search_fields = ['name','sex','age']


# Register your models here.
admin.site.register(bookinfo,bookinfostyle)
admin.site.register(roleinfo,roleinfostyle)


