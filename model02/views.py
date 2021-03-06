from django.db.models.query import RawQuerySet
from django.http import HttpResponse
from django.shortcuts import render

# linux 之父   垃圾的程序愿担心代码   优秀的程序担心的数据结构
# 怎么样把这些模型之间的关系组织好   映射关系    表与表之间的关系   模型与模型之间的关系
# 三种
#  一对一（）    一对多（多对一）  多对多

# Create your views here.
from model02.models import Emp, Dept


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

'''
默认情况下 把所有的字段重新赋值一遍
update_fields  指定更新的字段

'''


def update(request):
    # select * from emp  where
    emp = Emp.objects.get(emp_no=1)
    emp.emp_name = '老宋'
    emp.sal = 1200.00
    emp.save(update_fields=['emp_name', 'sal'])
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

def delete(request):
    emp = Emp.objects.get(pk=1, is_delete=0)
    emp.is_delete = 1
    emp.save()
    return render(request, 'index.html', {'msg': 'success'})


'''
F8  执行下一行代码
F7  表示进入方法或者函数
F9  表示执行下一个段点
SELECT `emp`.`emp_no`, `emp`.`emp_name`, `emp`.`job`, `emp`.`mgr`, `emp`.`hire_date`, `emp`.`sal`, `emp`.`comm`, `emp`.`dept_no`, `emp`.`is_delete` FROM `emp`

'''


# limit分页
def find(request):
    # emps = Emp.objects.all()[0:1]
    # print(emps)
    # emps = Emp.objects.filter(job='it', emp_no=3)
    # for emp in emps:
    #     print(emp.emp_name)

    # emps = Emp.objects.exclude(job='经纪人')
    # for emp in emps:
    #     print(emp.emp_name)
    # 升序  asc  降序- desc

    # emps = Emp.objects.all().order_by('-hire_date', 'emp_name')

    # select  emp_name, emp_no FROM  EMP  WHERE
    #
    # emps = Emp.objects.values('emp_name', 'emp_no')
    #
    # for emp in emps:
    #     print(emp['emp_name'])
    #     print(emp['emp_no'])

    # emps = Emp.objects.values_list('emp_name', flat=True)
    # emps = Emp.objects.values_list('emp_name', 'emp_no')
    # # ['test1',]
    # for emp in emps:
    #     print(emp[0])
    #     print(emp[1])
    # emps = Emp.objects.values_list('emp_name', 'emp_no',named= True)

    qs = Emp.objects.raw("select emp_no,emp_name from emp  where  job='%s'", ['it'])
    objects = raw_tools(qs)
    for obj in objects:
        print(obj['emp_name'])

    return HttpResponse('11111')


def other(request):
    # 查询员工姓名包含小的所有员工信息   sql语句 like %小%
    # emps = Emp.objects.filter(emp_name__contains='小')

    # 查询所有的员工姓名以老开头的   like 老%
    # startswith  区分大小写
    # istartswith  不区分大小写
    # endswith     区分大小写
    # iendswith    不区分大小写

    emps = Emp.objects.filter(job__iendswith='it')

    for emp in emps:
        print(emp.emp_name)

    # emps = Emp.objects.filter(emp_name__istartswith='老')

    # 范围操作     between  and
    # 工资范围在1000到2000之间的
    #  sal__range =[1000.00,2000.00]

    return HttpResponse('1111')


def raw_tools(raw_query_set):
    if isinstance(raw_query_set, RawQuerySet):
        li = []
        result = []
        for item in raw_query_set:
            li.append(item.__dict__)

        for obj in li:
            del obj['_state']
            result.append(obj)

    return result


def get_or_create(request):
    # try:
    #     emp=  Emp.objects.get(emp_name='test10', job='it')
    # except :
    #     Emp.objects.create(emp_name='test10', job='it')
    # pass
    emp = Emp.objects.update_or_create(default={'emp_name': 'test11'}, emp_name='小王')
    print(emp)
    return HttpResponse('111')


def update_or_create(request):
    # try:
    #     emp=  Emp.objects.get(emp_name='test10', job='it')
    # except :
    #     Emp.objects.create(emp_name='test10', job='it')

    emp = Emp.objects.update_or_create(default={'emp_name': 'test11'}, emp_name='小王')
    print(emp)
    # emp = Emp.objects.get(pk=1)
    # print(emp)

    return HttpResponse('111')


def batch_save(request):
    dept1 = Dept(dept_name='it', loc='武汉')
    dept2 = Dept(dept_name='财务', loc='武汉')
    objs = [dept1, dept2]
    #
    # 101     一次插入  batch = len(objs)
    Dept.objects.bulk_create(objs, batch_size=100)
    return HttpResponse('1111')


from django.db.models import Sum, Avg, Max, Min, Count, Q, F


def test_aggregate(request):
    # sum = Emp.objects.aggregate(Sum('sal'))
    # print(sum['sal__sum'])

    count = Emp.objects.aggregate(count=Count('emp_name'))
    print(count)
    return HttpResponse('1111')


def q_f(request):
    # 当两个q对象使用连操作符会生成一个新的Q对象

    name_q = Q(emp_name='小王')
    q = Q(job__icontains='it') | name_q
    # 等价于
    # emps = Emp.objects.filter(Q(emp_name='小王1') |Q(job='it'))
    # emps = Emp.objects.filter(q)
    # Emp.objects.filter(emp_name='',job='it')
    # emps = Emp.objects.filter(Q(emp_name='小王1') & Q(job='it'))
    Emp.objects.filter(~Q(job='it'))

    # for emp in emps:
    #     print(emp.emp_name)
    # emps = Emp.objects.all()
    # for emp in emps:
    #     emp.sal *= 12
    #     print(emp.sal)
    #
    # emp = Emp.objects.get(emp_name='老宋')
    # emp.sal -= 1000.00
    # emp.save()
    # 已有的字段上面进行运行
    #
    Emp.objects.filter(emp_name='老宋').update(sal=F('sal') - 1000.00)
    # Emp.objects.filter(sal=F('sal') * 12)

    #  select
    # update emp set  sal = 200.00

    return HttpResponse('1111')


"""
select sal * 12 from  emp
"""
