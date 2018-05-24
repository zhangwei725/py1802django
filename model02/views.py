from django.shortcuts import render

# Create your views here.
from model02.models import Emp


# save()  对象方法
# create()  类方法
def add(request):
    emp = Emp(emp_name='小王2',
              job='it',
              mgr=11,
              sal=1000.00,
              comm=500.00,
              dept_no=1)

    # emp = Emp()
    # emp.emp_name = '小王'
    # insert into emp() values
    emp.save()

    return render(request, 'index.html', {'msg': 'success'})


# orm  面向对象的思想操作数据库
def create(request):
    # insert into
    Emp.objects.create(emp_name='test1',
                       job='it',
                       mgr=11,
                       sal=1000.00,
                       comm=500.00,
                       dept_no=1)
    return render(request, 'index.html', {'msg': 'success'})


"""
修改对象
1> 从数据取出记录
2> 通过查询返回的对象做修改
3> 在保存

"""
def update(request):
    # select * from emp  where
    emp = Emp.objects.get(emp_no=1)
    emp.emp_name = '老宋'
    emp.sal = 1200.00
    emp.job = '经纪人'
    emp.save()
    # Emp.objects.get(pk=1)
    return render(request, 'index.html', {'msg': 'success'})


def update1(request):
    # 单条数据修改
    # Emp.objects.filter(emp_no=1).update(comm=1.00)
    # 如果是多个就批量的更新数据
    Emp.objects.filter(job='it').update(comm=1000.00)

    return render(request, 'index.html', {'msg': 'success'})


# 在公司一般的情况假删除
# 在表里添加一个字段    is_delete 1 表示删除  0 存在

# select *  from  emp where  name=''  and  is_delete=0

# def delete(request):
#     emp = Emp.objects.get(pk=1)
#     emp.delete()
#     return render(request, 'index.html', {'msg': 'success'})
#     学习能力   解决问题能力    90% 在debug   10% copy 改
# 假删除
def delete(request):
    emp = Emp.objects.get(pk=1, is_delete=0)
    emp.is_delete = 1
    emp.save()
    return render(request, 'index.html', {'msg': 'success'})
