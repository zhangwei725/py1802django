from django.conf.urls import url

from views01 import views

# (?P<page>\d+)  {'page':\d+,'size'：\d+}
from views01.views import Login

urlpatterns = [
    url(r'base/', views.base),
    url(r'^list/(\d+)/(\d+)/$', views.list),
    url(r'^list1/(?P<page>\d+)/(?P<size>\d+)/$', views.list1, name='list'),
    url(r'^list2/', views.list2),
    # cbv的注册方式
    url(r'^cbv/', Login.as_view()),
    url(r'login/', views.login),
    url(r'login1/', views.login1),

]
