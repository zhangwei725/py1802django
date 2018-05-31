from django.shortcuts import render

# Create your views here.

# 导航条
# 首页 | 机器 | 手机
from temp02.models import Shop


def tag_if(request):
    nav_list = ['女装', '母婴', '美妆', '国际', '男装']
    num = 1
    # user = {'name': '123132', 'num': 10}
    user = {}
    return render(request, 'temp02/nav.html', locals())


def other(request):
    if request.method == 'POST':
        keyword = request.POST.get('search')
        shops = Shop.objects.filter(name__icontains=keyword)
    return render(request, 'temp02/other.html', locals())


def test_static(request):
    return render(request, 'temp02/static.html')


def ext(request):
    return render(request, 'child.html')


"""
过滤器
"""

import datetime

"""
日期格式化  
Y 4位数表示 2018      
y 两位表示 18  
m 前导加0  03
M 表示  3
d 前面加0  01 - 31
D 
H 表示24小时制
h 12小时制
i  00-59
s  秒数 00-59





"""


def filter_sample(request):
    context = {'msg': None,
               'create_date': datetime.datetime.now(),
               'num': '1',
               'tag': 'hello'
               }
    return render(request, 'filter/sample.html', context)


def custom_filter(request):
    return render(request, 'custom_tags.html')
