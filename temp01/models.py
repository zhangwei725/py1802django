from django.db import models


# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=64)



