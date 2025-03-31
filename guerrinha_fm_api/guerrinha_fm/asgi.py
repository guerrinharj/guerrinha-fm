import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guerrinha_fm.settings")

# Create the basic application
django_asgi_app = get_asgi_application()

# Delay the import until AFTER apps are loaded
def get_application():
    from tracks.routing import websocket_urlpatterns

    return ProtocolTypeRouter({
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    })

application = get_application()
