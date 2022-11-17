from django.contrib import admin

from student.models import Specialization, Student
class Admin(admin.ModelAdmin):
    list_display = ('user','fees_paid','date_added')

# admin.site.register(Student,Admin)
# admin.site.register(Specialization)

