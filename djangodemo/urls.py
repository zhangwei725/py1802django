from django.conf.urls import url, include
from django.contrib import admin

from views01 import views

"""

import方式导入模块  
1> 整个文件导入
2> 创建独立的命名空间 作用域 内置 全局  闭包 局部

创建两个独立的命名空间    urls.py
"""
# http://127.0.0.1:8000/


# 在浏览器输入的地址
urlpatterns = [
    url('admin/', admin.site.urls),
    url('model/', include('model02.urls')),
    url('hello/', include('hello.urls')),
    url('model03/', include('model03.urls')),
    url(r'views/', include('views01.urls'))

    # http://127.0.0.1:8000/view/

]
