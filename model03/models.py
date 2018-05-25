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


class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=32, db_index=True, unique=True)

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

    # 使用一对多 就把外键设置唯一 就类似与一对一的效果
    # stu  = models.ForeignKey(unique=True)

    #
    class Meta:
        db_table = 'student_detail'
