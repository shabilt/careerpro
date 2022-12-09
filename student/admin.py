from django.contrib import admin

from student.models import Specialization, Student
class Admin(admin.ModelAdmin):
    list_display = ('user','fees_paid','date_added')

# admin.site.register(Student,Admin)
# admin.site.register(Specialization)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
    'auto_id',
    
    )
admin.site.register(Student,StudentAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('auto_id','title')
admin.site.register(Specialization,SpecializationAdmin)