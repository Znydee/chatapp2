#"""
#ASGI config for chatapp project.

#It exposes the ASGI callable as a module-level variable named ``application``.

#For more information on this file, see
#https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
#"""

#import os
#from channels.routing import ProtocolTypeRouter
#from django.core.asgi import get_asgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')

#application = get_asgi_application()
#application = ProtocolTypeRouter({
#    "http": get_asgi_application(),
#    # Just HTTP for now. (We can add other protocols later.)
#})
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp2.settings')
django_asgi_app = get_asgi_application()
import chat.routing
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})