from django.conf.urls import url

from model02 import views

# http://127.0.0.1:8000/model/emp
urlpatterns = [
    url('add/', views.add),
    url('add/', views.add),
    url('create/', views.create),
    url('update/', views.update),
    url('update1/', views.update1),
    url('delete/', views.delete),
]
