from django.contrib import admin
from django.urls import path

from hello import views

"""

import方式导入模块  
1> 整个文件导入
2> 创建独立的命名空间 作用域 内置 全局  闭包 局部

创建两个独立的命名空间    urls.py


"""

# 在浏览器输入的地址 http://127.0.0.1:8000/hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello)
]
