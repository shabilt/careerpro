
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Chat,ChatMember,Message
from chat.serializers import MessageSerializer
from asgiref.sync import sync_to_async

 
 
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self,):
        user = self.scope["user"]
        print(user)
        self.roomGroupName = "user_" + str(user)
        print(self.roomGroupName)
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
        # print(data)
        # print(data)
        # print(self.scope)


        # print(self.scope["user"])
        data["sender_id"] = self.scope["user"].id

        # await self.channel_layer.group_add(
        #     "grpppp",
        #     self.channel_name
        # )
        # await self.accept()


        # sync_to_async(Message.objects.all())()
        # sync_to_async(Message.objects.create(
        #     **data
        # ))(data)
        

        await sync_to_async(Message.objects.create)(**data)

        # for user in users:
        #     print(user)

        # serializer = MessageSerializer(data=data)
        # if(serializer.is_valid()):
        #     serializer.save()
        # else:
        #     print("msg not valid")
        #     print(serializer)


        # TokenAuthentication.authenticate_credentials()

        # message = text_data_json["message"]
        # username = text_data_json["username"]
        # username = "hashid"

        # @sync_to_async
        # def get_all_members(chat_id):
        #     return ChatMember.objects.filter(chat=chat_id)

        # for member in await get_all_members(data["chat_id"]):
        #     print(member)

        @sync_to_async
        def get_all_members(chat_id):
            members =  ChatMember.objects.filter(chat=chat_id)
            for member in members:
                print(member)
                print("user_" + str(member.account.username))
                x = self.channel_layer.group_send(
                "user_" + str(member.account.username),{
                    "type" : "sendMessage" ,
                    "data" : {**data}
                })
                print(x)
        
        await get_all_members(data["chat_id"])
        # await sync_to_async(Message.objects.create)(**data)

        # async def foo():
        # for member in await get_all_members(data["chat_id"]):
        #     print(member)
        #     await self.channel_layer.group_send(
        #     "user_" + str(member.member.username),{
        #         "type" : "sendMessage" ,
        #         "data" : {**data}
        #     })
        # foo()
                
        # for member in members:
        #     await self.channel_layer.group_send(
        #         "user_" + str(member.user.username),{
        #             "type" : "sendMessage" ,
        #             "data" : {**data}
        #         })
    async def sendMessage(self , event) :
        print("sendMessage ss")


        print(event["data"])
        await self.send(text_data = json.dumps(event["data"]))

