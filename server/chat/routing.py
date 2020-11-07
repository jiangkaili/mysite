# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/11/8 2:19 上午
# @File    : routing.py

from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
