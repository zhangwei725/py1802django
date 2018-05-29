from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from views01.models import User


def base(request):
    return HttpResponse('base')


'''
一种写法 直接在路径里匹配   直接需要在视图函数里定义参数
另外一种写法 作为参数传递   request 去获取相应的数据

url :     url(r'^list/(\d+)/(\d+)/$', views.list)
视图函数　　　list(request, page, size)
访问路径　　　 http://127.0.0.1:8000/views/list/2/10/ 
'''


def list(request, page, size):
    return HttpResponse("当前页数%s 每页%s条" % (page, size))


'''
urls.py   :  url(r'^list1/(?P<page>\d+)/(?P<size>\d+)/$', views.list1)
def list1(request, page, size):
访问的路径   http://127.0.0.1:8000/views/list2/2/10/

'''


def list1(request, page, size):
    # request.GET.get('page')
    return HttpResponse("当前页数%s 每页%s条" % (page, size))


"""
url.py    url(r'^list2/$', views.list2),
views.py  def list2(request):
访问的路径   http://127.0.0.1:8000/views/list2/?page=1&size=10
"""


def list2(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        size = request.GET.get('size')
    elif request.method == "POST":
        print('POSt')
    return HttpResponse("当前页数%s 每页%s条" % (page, size))


"""
控制层   
FBV     function base  view
CBV  class  base View

"""

#  支持 http1.1的8中请求
"""

url  url(r'^cbv/', Login.as_view()),

视图对象   def get(self, request):对应get请求
         def post(self, request): 对应post请求
访问的url         

"""


class Login(View):
    # get请求
    def get(self, request):
        print(request)
        print()
        return HttpResponse('cbv')

    def post(self, request):
        pass
    #
    # def put(self):
    #     pass
    #
    # def delete(self):
    #     pass


#  接受用户请求

'''
用户发送请求---->uwsgi----> urls----->views--->model---->返回数据(views)--->template 渲染--->views响应
'''

"""
GET
"""


# ?

# 127.0.0.1:8000/views01/login?username=xiaoming&password=123456
def login(request):
    msg = None
    # 判断请求方式     GET POST 必须大写
    if request.method == 'GET':
        #   request.GET   返回的是 字典形式的  QueryDict
        # QueryDict      get(key,default )   获取单个值
        # QueryDict      getlist(key,default ) #  多选  多文件
        username = request.GET.get('username', default='1')
        password = request.GET.get('password')
        # 判断用户输入的 用户名或者password 是否为空
        if username and password:
            qs = User.objects.filter(username=username)
            if len(qs) > 0:
                user = qs.first()
                if user.password == password:
                    msg = '登录成功'
                else:
                    msg = '密码错误'
                pass
            else:
                msg = '账号不存在'
        else:
            msg = '账号不存在'
    return HttpResponse(msg)


# 响应用户的请求

def login1(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        return render(request, 'index.html', {'username': username})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ck = request.POST.getlist('ck')
        print(ck)
        try:
            User.objects.get(username=username)
        except User.DoesNotExist as e:
            User.objects.create(username=username, password=password)
        return HttpResponse('13213')


# http://127.0.0.1:8000/list
def page(request):
    page = request.GET.get('page', default=1)
    size = request.GET.get('size', default=10)


# http://127.0.0.1:8000/list
def meta(request):
    # request.path
    server_name = request.META['SERVER_NAME']
    # 获取请求体的长度
    length = request.META['CONTENT_LENGTH']
    host = request.META['HTTP_HOST']
    port = request.META['SERVER_PORT']

    return HttpResponse('1111', content_type='application/json')


"""
# 一种返回模板  TemplateResponse  
简写方式  render
1> 语法格式
render(reqeust,template_name,context=None,status=200,use=None)
2>参数说明
request (必要参数)  
template_name 模板的名称 注意如果在模板下面有新建了文件夹使用 目录名/模板名  例如views/test.html
3>context    字典对象 把一组字典的值添加到模板中去,默认是空
#   返回json数据
"""


def resp(request):
    # context = {'username': '123',
    #            'hehe': 'http://ww1.sinaimg.cn/large/0065oQSqly1frqscr5o00j30k80qzafc.jpg'
    #             ,'password':'123'
    #            }
    username = '123'
    hehe = 'http://ww1.sinaimg.cn/large/0065oQSqly1frqscr5o00j30k80qzafc.jpg'
    password = '123'
    return render(request, 'veiws/test.html', locals())


