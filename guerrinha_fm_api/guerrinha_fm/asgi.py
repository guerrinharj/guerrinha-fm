import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guerrinha_fm.settings")

django_asgi_app = get_asgi_application()

def get_application():
    # ✅ Lazy imports
    from tracks.routing import websocket_urlpatterns as tracks_ws
    from chat.routing import websocket_urlpatterns as chat_ws

    return ProtocolTypeRouter({
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(
                tracks_ws + chat_ws
            )
        ),
    })

application = get_application()
