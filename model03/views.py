from django.http import HttpResponse

from model03.models import Student, StudentDetail

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

    # stu = Student()
    # stu.stu_name = '左强大神'
    # stu.save()
    # 第二种 通过id的方式
    # 属性_id
    StudentDetail.objects.create(student_id=3, email='123@163.com', no='91')
    return HttpResponse('123132131321')
