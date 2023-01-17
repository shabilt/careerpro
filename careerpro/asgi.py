import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'careerpro.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter
from chat import routing
from main.middleware import TokenAuthMiddleware


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
    }
)