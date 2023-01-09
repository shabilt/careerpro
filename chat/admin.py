from django.contrib import admin

from chat.models import Chat, ChatMember,Message,MessageFile
# class Admin(admin.ModelAdmin):
#     list_display = ('user','fees_paid','date_added')

# admin.site.register(Student,Admin)
# admin.site.register(Specialization)


class ChatAdmin(admin.ModelAdmin):
    list_display = (
    'id',"name",
    
    )
admin.site.register(Chat,ChatAdmin)

class ChatMemberAdmin(admin.ModelAdmin):
    list_display = ('id','account')
admin.site.register(ChatMember,ChatMemberAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','chat','sender')
admin.site.register(Message,MessageAdmin)

class MessageFileAdmin(admin.ModelAdmin):
    list_display = ('id','account','msg_file')
admin.site.register(MessageFile,MessageFileAdmin)