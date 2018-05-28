from django.db import models

'''
映射   两张或者两张以上的表

'''
"""
1> 两张表
2> 确定主表（学生表） 子表（详情表）  
3> 外键 一般设置在子表上面（实质就是在子表上面添加一个字段，但是这个字段必须参照主表的某一列）
4> 一般情况下参照的列是主表的主键

备注 > 设置外键的条件参考的字段必须是唯一

"""

"""
1>多对多关系肯定有第三张表
1> 也可以采用两个一对多去实现

"""

"""
through
作用 当你不想使用系统自带的模型类去创建时候 可以自己定义第三方表的模型对象

"""


# class StudentRoom(models.Model):
#     stu_room_id = models.AutoField(primary_key=True)
#     room = models.ForeignKey('Room')
#     stu = models.ForeignKey('Student')
#
#     class Meta:
#         db_table = 'student_room_middle'


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=32)

    class Meta:
        db_table = 'room'


class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=32, db_index=True, unique=True)
    # 多对多
    """
    参数说明
    to 必须
    to_filed 
    related_name  主要用户主表查询字表时候的字段 默认是 
    db_table   制定第三方张的名称 默认是 子表_主表
    through  自己指定第三个模型对象
    """
    room = models.ManyToManyField(Room)

    """
     参数说明

     to 主表 对应类的名称

     on_delete  当主表的数据删除的数据的时候子表如何处理数据
     related_name   默认是类名小写_set 主表属性 
     to_field  参照主表的字段  默认主键

     """

    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='students', to_field='id',
                                db_column='t_id')

    # 使用一对多 就把外键设置唯一 就类似与一对一的效果
    # stu  = models.ForeignKey(unique=True)
    class Meta:
        db_table = 'student'


class StudentDetail(models.Model):
    stu_detail_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64, null=True)
    no = models.CharField(max_length=128, null=True)
    """
    参数说明
    to,  主模型的名称（类名）必须   
    on_delete= None, 当主表的数据删除的数据的时候子表如何处理数据
            CASCADE  子表也删除
            SET_NULL  子表的数据不删除 外键字段设置null  
    
    to_field=None,  参考字段 默认就主表的主键
    
    其他   
      外键的名称  默认的情况  属性名_id 
      
    """
    student = models.OneToOneField('Student', on_delete=models.CASCADE, db_column='stu_id')

    # 建立一对多的关系
    # to, on_delete=None, related_name=None,  to_field=None,

    #
    class Meta:
        db_table = 'student_detail'


#  一对多
# 一的一方的主表 多的一方是从表，多的一方建外键


class Teacher(models.Model):
    tea_name = models.CharField(max_length=32, unique=True, db_index=True)

    class Meta:
        db_table = 'teacher'
