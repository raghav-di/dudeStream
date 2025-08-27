import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import core.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collabview.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # This tells Channels to use the URLs from your core/routing.py file
            core.routing.websocket_urlpatterns
        )
    ),
})