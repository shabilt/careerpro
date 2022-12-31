from urllib import response
from django.shortcuts import get_object_or_404, render
# from main.permissions import IsUser
from chat.serializers import ChatSerializer,ChatMemberSerializer,MessageSerializer
from .models import *
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from  rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from main.functions import get_auto_id





from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})



class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer
    # queryset = Chat.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    # search_fields = ['student__user__username','student__user__first_name','student__user__last_name']
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        chat_member = ChatMember.objects.filter(account=user).prefetch_related('chat')

        print(chat_member)
        return chat_member.chat.objects.filter()

    def list(self, request):
        # queryset = Chat.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)




class ChatMemberViewSet(ModelViewSet):
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    # search_fields = ['student__user__username','student__user__first_name','student__user__last_name']
    
    def list(self, request):
        queryset = ChatMember.objects.all()
        serializer = ChatMemberSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request, *args, **kwargs):
        serializer = ChatMemberSerializer(data=request.data ,context={'request': self.request})
        if(serializer.is_valid() and (not ChatMember.objects.filter(account=request.user).exists())):
            serializer.save(account = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {"error":"Already exists !"}
            return Response(data,status=status.HTTP_403_FORBIDDEN)




class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    # search_fields = ['student__user__username','student__user__first_name','student__user__last_name']
    
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)





# Create your views here.

