from django.shortcuts import render
from hello.models import Shop


# 控制
# Create your views here
# views 调用model
# 数据库只支持sql语句
# 生产sql语句
def hello(request):
    # select * from shop
    shop = Shop.objects.all().first()
    # model层和template桥梁
    # template
    context = {'shop': shop}
    return render(request, 'users.html', context)
