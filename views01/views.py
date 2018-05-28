from django.http import HttpResponse

# Create your views here.
from django.views import View


def base(request):
    return HttpResponse('base')


'''
一种写法 直接在路径里匹配   直接需要在视图函数里定义参数
另外一种写法 作为参数传递   request 去获取相应的数据

url :     url(r'^list/(\d+)/(\d+)/$', views.list)
视图函数　　　list(request, page, size)
访问路径　　　 http://127.0.0.1:8000/views/list/2/10/ 
'''

def list(request, p, s):
    # request.GET.get('page')
    return HttpResponse("当前页数%s 每页%s条" % (p, s))


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
