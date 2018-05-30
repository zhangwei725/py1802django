from django.conf.urls import url, include

from model03 import views

"""

import方式导入模块  
1> 整个文件导入
2> 创建独立的命名空间 作用域 内置 全局  闭包 局部

创建两个独立的命名空间    urls.py
"""
# 在浏览器输入的地址
urlpatterns = [
    url('save/', views.save),
    url('update/', views.update),
    url('^find/&', views.find),
    url('fk_save/', views.fk_save),
    url('^fk1/$', views.fk_find),
    url('student/', views.students),
    # /detail/1
    url(r'^detail/(?P<stu_id>\d+)/$', views.student_detail)
]
