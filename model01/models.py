from django.db import models

# Create your models here.models.py
#  类  -------> 表
#  类名 对应表名
#  属性 对应列名
#   一个对象 对应一条记录
# 默认情况下通过模型生成表时候  模块名+类名


"""
每个必须有主键   id


所有的模型层的对象都要继承 models.Model
如果你不定义主键  默认会主键 以id命名   设置外检   两个表   主表  从表(在设置外键 实质字段)  把主表主键作为从表外键

"""

"""
定义好模型之后迁移数据
"""


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'person'


class Shop(models.Model):
    # AutoField  自动增长  primary_key 主键
    shop_id = models.AutoField(primary_key=True)
    #  表示字符串字段varchar(64)---对应数据的类型 varchar(64)
    #
    name = models.CharField(max_length=64)

    create_date = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_state = models.BooleanField()
    # float(10,2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # models.FileField
    # models.ImageField