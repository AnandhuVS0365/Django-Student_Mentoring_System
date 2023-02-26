from django.contrib import admin
from home.models import *

# Register your models here.

class menteelistfields(admin.ModelAdmin):
    list_display=('mentee_name','mentee_email','mentee_password')
class usertypefields(admin.ModelAdmin):
    list_display=('user','type')
class menteefields(admin.ModelAdmin):
    list_display=('mentee_name','mentor_name')
class mentorfields(admin.ModelAdmin):
    list_display=('mentor_name','mentor_email','mentor_password')




admin.site.register(menteelist,menteelistfields)
admin.site.register(UserType,usertypefields)
admin.site.register(mentee,menteefields)
admin.site.register(mentor,mentorfields)
admin.site.register(assignment)
admin.site.register(accommodation)
admin.site.register(academicqualification)
admin.site.register(counselling)

