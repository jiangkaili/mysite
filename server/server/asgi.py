# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/11/8 2:47 上午
# @File    : asgi.py


"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()
application = get_default_application()