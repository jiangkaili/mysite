# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/11/8 2:02 上午
# @File    : urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
