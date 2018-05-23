from django.contrib import admin

# Register your models here.
# 注册模型
from model01.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


# admin.register(Shop)
