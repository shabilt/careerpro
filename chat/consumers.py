

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Chat,ChatMember,Message
from chat.serializers import MessageSerializer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

 
 
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self,):
        user = self.scope["user"]
        self.roomGroupName = "user_" + str(user)

        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName ,
            self.channel_layer
        )
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        print(data)
        print(self.scope)

        data["sender_id"] = self.scope["user"].id

        msg_data ={
                'chat_id': data["chat"],
                'sender_id': self.scope["user"].id,
                'content':data["content"]
            }

        print(msg_data)

        await sync_to_async(Message.objects.create)(**msg_data)

        
        members = data["chat_members"]

        print(members)
        for member in members:
            await self.channel_layer.group_send(
                "user_" + str(member),{
                    "type" : "sendMessage" ,
                    "data" : {**data}
                })

    async def sendMessage(self , event) :
        print("sendMessage ss")


        print(event["data"])
        await self.send(text_data = json.dumps(event["data"]))

