from django.conf.urls import url
from temp01 import views

urlpatterns = [
    url('base/', views.temp_base),
    url('list/', views.user_list),
    url('for_dic/', views.for_dict),
    url('nav/', views.for_nav)
]
