from django.http import HttpResponse
from django.shortcuts import render

from model03.models import Student, StudentDetail, Teacher, Room

"""

保存学生详情
约束 强加在表的规则和条件 主要确保数据库的数据满足业务需求,保证数据的完整性

"""
"""

一对一 保存
1> 当我们去往子表添加数据的时候，确保主表记录
2>  

"""


# 创建字段的是属性_id
def save(request):
    # stu = Student()
    # stu.stu_name = '左强大神'
    # stu.save()
    # # 第一种   stu 必须是对象
    # StudentDetail.objects.create(student=stu, email='123@163.com', no='91')

    stu = Student()
    stu.stu_name = '左强大神'
    stu.save()
    # 第二种 通过id的方式保存子表
    # 属性_id
    StudentDetail.objects.create(student_id=stu.pk, email='123@163.com', no='91')

    return HttpResponse('123132131321')


# 通过主表的数据修改子表的数据
def update(request):
    # 从request的get请求获取学生的id
    stu_id = request.GET.get('stu_id')
    email = request.GET.get('email')

    stu = Student.objects.get(pk=int(stu_id))

    stu_de = StudentDetail.objects.get(student_id=stu.stu_id)
    stu_de.email = email
    stu_de.save()

    return HttpResponse('123132131321')


'''

第一种情况 通过主表查子表

'''


def find(request):
    stu_id = request.GET.get('id')
    # stu = Student.objects.get(pk=int(stu_id))
    # # 隐藏属性 子表的
    # print(stu.stu_name, stu.studentdetail.email, stu.studentdetail.no)

    """
    第二种情况  通过字表查询主表
    :param request:
    :return:
    """
    stu_de = StudentDetail.objects.get(pk=int(stu_id))
    print(stu_de.student.stu_name)

    return HttpResponse('123132131321')


"""
通过主表查子表
1>先查询主表
2>通过主表实例.字表类名小写_set
通过子表查主表   

"""


def fk_find(request):
    # teacher = Teacher.objects.get(pk=1)
    # teacher.setudents.all()
    stu = Student.objects.filter(stu_name__contains='小').first()
    # stu.teacher.tea_name
    # stu.teacher.id
    # stu.stu_name

    return HttpResponse('123132131321')


def fk_save(request):
    teacher = Teacher.objects.create(tea_name='隔壁小张')
    print(teacher.id)
    for index in range(10):
        Student(stu_name='test' + str(index), teacher_id=teacher.pk).save()

    return HttpResponse('123132131321')


def many_add(request):
    # Room.objects.create(room_name='实训1')
    # Room.objects.create(room_name='实训2')
    #
    # tea = Teacher.objects.create(tea_name='小张')
    #
    # Student.objects.create(stu_name='小明', teacher=tea)
    # Student.objects.create(stu_name='小红', teacher=tea)
    #     通过子表添加主表数据
    """
        1> 获取子表的学生对象
        2> 获取主表数据的对象 all() filter()
        3> 利用子表的关联字段.add(*QuerySet)
     """
    # stu = Student.objects.get(stu_id=1)
    # room = Room.objects.all()
    # stu.room.add(*room)

    #  通过主表添加子表数据
    room = Room.objects.get(room_id=1)
    stu_list = Student.objects.all()
    room.student_set.add(*stu_list)

    return HttpResponse('123132131321')


def many_find(request):
    """
    已知子表的某个条件 去查询主表的相关信息
    :param request:
    :return:
    """
    # 通过子表查询主表
    # 方式一
    # student = Student.objects.get(pk=1)
    # rooms = student.room.all()
    # 方式二
    # Room.objects.filter(student__stu_id=1)

    # 通过主表查询子表
    rooms = Room.objects.filter(room_name__contains='实训')

    for room in rooms:
        stu_list = room.student_set.all()
        for stu in stu_list:
            print(room.room_name)
            print(stu.stu_name)


def students(request):
    students = Student.objects.all()
    return render(request, 'temp/student.html', locals())


"""
需要知道学生的id
"""


def student_detail(request, stu_id):
    stu_detail = StudentDetail.objects.filter(student__stu_id=int(stu_id)).first()
    return render(request, 'temp/student_detail.html', locals())
