from django.conf.urls import url, include
from django.contrib import admin

from hello import views
from model01 import views

"""

import方式导入模块  
1> 整个文件导入
2> 创建独立的命名空间 作用域 内置 全局  闭包 局部

创建两个独立的命名空间    urls.py
"""
# 在浏览器输入的地址
urlpatterns = [
    url('admin/', admin.site.urls),
    url('test/', views.test),
    url('model/', include('model02.urls')),
    url('model03/', include('model03.urls')),
]
