from django.contrib import admin
from testapp.models import UserProfile, History
# Register your models here.

class CustomUser(admin.ModelAdmin):
    list_display = ['name','email','balance','mob_no','password']
    list_display_links = ['name','email','balance','mob_no','password']

class CustomHistory(admin.ModelAdmin):
    list_display = ['status','amount','additional_msg','time','user']
    list_display_links = ['status','amount','additional_msg','time','user']


admin.site.register(UserProfile,CustomUser)
admin.site.register(History,CustomHistory)
