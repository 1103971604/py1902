from django.db import models

# Create your models here.
class bookinfo(models.Model):
    title=models.CharField(max_length=20,verbose_name='书名')
    put_time=models.DateTimeField(auto_now_add=True,verbose_name='出版日期')

    def __str__(self):
        return self.title

class roleinfo(models.Model):
    name=models.CharField(max_length=20,verbose_name='姓名')
    age=models.IntegerField(verbose_name='年龄')
    sex=models.CharField(max_length=10,choices=(('1','男'),('2','女')),verbose_name='性别')
    book=models.ForeignKey(bookinfo,on_delete=models.CASCADE,verbose_name='所属丛书')

    def __str__(self):
        return self.name