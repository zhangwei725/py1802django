from django.db import models


# Create your models here.
class Shop(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        db_table = 't_shop'
