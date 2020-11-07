# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/11/8 2:07 上午
# @File    : routing.py


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
