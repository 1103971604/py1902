from django.shortcuts import render
# 为了返回 引入 HttpResponse
from django.http import HttpResponse

from .models import bookinfo,roleinfo

# Create your views here.

def index(request):
    # return HttpResponse('主页')
    return render(request,'demo2/index.html')
def booklist(request):
    # return HttpResponse('书籍列表')

    books=bookinfo.objects.all() #查询所有书
    return render(request, 'demo2/booklist.html',{'books':books})

def role(request,bookid):
    # return HttpResponse('角色列表')

    book=bookinfo.objects.get(pk=bookid)
    return render(request, 'demo2/role.html', {'book':book})


