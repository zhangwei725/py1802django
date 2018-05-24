from django.db import models


# Create your models here.

class Emp(models.Model):
    emp_no = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=15, db_index=True, unique=True)
    job = models.CharField(max_length=10)
    mgr = models.IntegerField(null=True)  # 正整數
    hire_date = models.DateTimeField(auto_now_add=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2)
    comm = models.DecimalField(max_digits=7, decimal_places=2)
    dept_no = models.IntegerField()
    is_delete = models.BooleanField(default=0)  # 1表示删除 0表示正常

    class Meta:
        db_table = 'emp'


class Dept(models.Model):
    dept_no = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=15, db_index=True)
    loc = models.CharField(max_length=50)

    class Meta:
        db_table = 'dept'
