from django import views
from django.urls import path
from rest_framework import routers
from .views import *

app_name = 'chat'




router = routers.DefaultRouter()
router.register('chat',ChatViewSet, basename='chat')
router.register('chat-member',ChatMemberViewSet, basename='chat_member')
router.register('message',MessageViewSet, basename='message')
router.register('message-file',MessageFileViewSet, basename='message_file')
# router.register('admin',AdminViewSet, basename='admin')



urlpatterns = [
    path("/", index, name="index"),
    # path("<str:room_name>/", room, name="room"),
    
]

urlpatterns += router.urls

