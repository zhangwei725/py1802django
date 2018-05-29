from django.conf.urls import url
from temp01 import views

urlpatterns = [
    url('base/', views.temp_base),
    url('list/', views.user_list)
]
