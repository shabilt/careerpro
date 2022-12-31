
# from django.urls import path , include
# from chat.consumers import ChatConsumer
 
# # Here, "" is routing to the URL ChatConsumer which
# # will handle the chat functionality.
# # websocket_urlpatterns = [
# #     path("", ChatConsumer.as_asgi()) ,
# # ]
# # print("routing / /")



# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.urls import path
# from main.middlewares import TokenAuthMiddleware
 
# application = ProtocolTypeRouter(
#     {
#         "websocket": TokenAuthMiddleware(
#             AllowedHostsOriginValidator(
#                 URLRouter(
#                 [ path("", ChatConsumer.as_asgi())]
#                 )
#             )
#         )
#     }
# )


from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
