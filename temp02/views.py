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
