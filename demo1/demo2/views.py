from django.shortcuts import render
# 为了返回 引入 HttpResponse  为了重定向 引入HttpResponseRedirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import bookinfo,roleinfo

# Create your views here.
#跳转主页
def index(request):
    # return HttpResponse('主页')
    return render(request,'demo2/index.html')
# 显示书籍信息
def booklist(request):
    # return HttpResponse('书籍列表')
    books=bookinfo.objects.all() #查询所有书
    return render(request, 'demo2/booklist.html',{'books':books})
# 显示书中角色
def role(request,bookid):
    # return HttpResponse('角色列表')
    book=bookinfo.objects.get(pk=bookid)
    return render(request, 'demo2/role.html', {'book':book})
# 删除图书
def delbook(request,bookid):
    bookinfo.objects.get(pk=bookid).delete()
    return HttpResponseRedirect('/demo2/booklist/')

# 删除角色
def delrole(request,roleid):

    role=roleinfo.objects.get(pk=roleid)
    id=role.book.id
    role.delete()
    return HttpResponseRedirect('/demo2/role/%s/'%(id,))
# 添加一本书
def addbook(request):
    if request.method=='GET':
        return render(request,'demo2/addbook.html')
    elif request.method=='POST':
        b1=bookinfo()
        b1.title=request.POST['bookname']
        b1.save()
        # return HttpResponse('重定向成功')
        return HttpResponseRedirect('/demo2/booklist/')
# 添加一个角色
def addrole(request,bookid):
    book = bookinfo.objects.get(pk=bookid)
    if request.method=='GET':
        return render(request,'demo2/addrole.html',{'book':book})
    if request.method=='POST':
        role=roleinfo()
        role.name=request.POST['username']
        role.age=request.POST['age']
        role.sex=request.POST['sex']
        role.book=book
        role.save()
        return HttpResponseRedirect('/demo2/role/%s/'%(book.id,))

# 修改书籍信息
def setbook(request,bookid):
    book=bookinfo.objects.get(pk=bookid)
    if request.method=='GET':
        return render(request,'demo2/setbook.html',{'book':book})
    elif request.method=='POST':
        book.title=request.POST['bookname']
        book.save()
        return HttpResponseRedirect('/demo2/booklist/')
# 修改 角色信息
def setrole(request,roleid):
    role1=roleinfo.objects.get(pk=roleid)
    if request.method=='GET':
        return render(request,'demo2/setrole.html',{'role':role1})
    if request.method=='POST':
        role1.name=request.POST['username']
        role1.age=request.POST['age']
        role1.sex=request.POST['sex']
        role1.save()
        return HttpResponseRedirect('/demo2/role/%s/'%(role1.book.id,))





