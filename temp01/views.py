from django.shortcuts import render

from temp01.models import User

"""
模板语法
1>基础变量
语法格式 {{变量名}}  字母数字_
2>
如果复杂对象   list   字典  元素   自定义对象
必须使用.语法
"""


def temp_base(request):
    li = ['http://ww1.sinaimg.cn/large/0065oQSqly1frqscr5o00j30k80qzafc.jpg',
          'http://ww1.sinaimg.cn/large/0065oQSqly1frmuto5qlzj30ia0notd8.jpg',
          'http://ww1.sinaimg.cn/large/0065oQSqly1frjd77dt8zj30k80q2aga.jpg',
          ]

    image_dict = {'img1': 'http://ww1.sinaimg.cn/large/0065oQSqly1frjd4var2bj30k80q0dlf.jpg',
                  'img2': 'http://ww1.sinaimg.cn/large/0065oQSqly1frja502w5xj30k80od410.jpg',
                  }
    user = User(img='http://ww1.sinaimg.cn/large/0065oQSqly1fri9zqwzkoj30ql0w3jy0.jpg')
    context = {'name': '小明',
               'age': 1,
               'imgs': li,
               'images': image_dict,
               'user': user,
               }

    return render(request, 'temp/temp_base.html', context)


def user_list(request):
    user_dict = User.objects.all()
    return render(request, 'temp/for.html', {'users': user_dict})


def for_dict(request):
    # dic = {'name': '小明', 'age': 10}
    dic = {}

    return render(request, 'temp/for_dict.html', locals())


def for_nav(request):
    nav_list = ['女装', '母婴', '美妆', '国际', '男装']
    return render(request, 'temp/for_dict.html', locals())
