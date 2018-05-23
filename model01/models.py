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
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'person'


"""
加快对数据特定的字段查询的速度的  
如果说经常要增删改不要加索引,因为降低增删改的效率
其次会占用磁盘


主键是唯一的 会自动创建索引

约束 表级约束  行约束

create  table  test(
id int(10)    primary key
name varchar(20)  not null  default,
age  int(3),
CONSTRAINT  [外键名]  primary key(id)













,



)


"""


# 主键是唯一的 会自动创建索引
class Shop(models.Model):
    # AutoField  自动增长  primary_key 主键
    shop_id = models.AutoField(primary_key=True)
    #  表示字符串字段varchar(64)---对应数据的类型 varchar(64)
    shop_name = models.CharField(max_length=64, null=False, db_index=True, unique=True, db_column='SHOPNAME')
    # 日期类型
    create_date = models.DateField(auto_now_add=True)
    # 日期和时间
    last_login = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default=0)
    #
    is_state = models.BooleanField()
    dsc = models.CharField(max_length=100, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='pid')
    # float(10,2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # models.FileField
    # models.ImageField
    #    约束  长度  索引  admin站点管理相关
    #     非空约束  唯一约束  默认值  外键约束
    #     索引

    class Meta:
        # 指定表名
        db_table = 'shop'
        verbose_name = '商品信息'
        verbose_name_plural = '商品列表'
