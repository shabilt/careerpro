import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'careerpro.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter
from main.middleware import TokenAuthMiddleware
from chat import routing


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
    }
)