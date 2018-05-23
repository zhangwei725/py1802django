from django.shortcuts import render

# Create your views here.


# ?type=1&page=1


# http:127.0.0.1:8000/test

from django.http import HttpResponse

from model01.models import Shop


def test(reqeust):
    # pserson = Person.objects.all()
    return render(reqeust, '', '')


def test_model(request):
    shop = Shop(is_state=True)
    shop.name = '手机1'
    shop.dsc = None
    # insert into
    shop.save()
    #
    # shop = Shop.objects.get(shop_id=1)
    # shop.name='测试数据1'
    # shop.price = 1000.00
    # shop.save()
    return HttpResponse('1111111')
