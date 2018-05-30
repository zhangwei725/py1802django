from django.conf.urls import url

from temp02 import views

urlpatterns = [
    url(r'tag_if/', views.tag_if, name='tag'),
    url(r'other/', views.other, name='other'),
    url(r'test_static/', views.test_static),
    url(r'ext/', views.ext),
]
