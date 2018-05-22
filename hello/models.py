from django.db import models

# Create your models here.

# 面向对象   对象 ----  类名   属性名
# 关系数据库  表        表名   列名

# orm  object  relation    mapping  对象映射关系

"""

"""


class Shop(models.Model):
    # 对应数据的主键
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    # max_digits 数字长度   decimal_places
    # flat(7,2)
    price = models.FloatField()

    def __str__(self):
        return self.sid
