from django.contrib import admin
from .models import*

# Register your models here.
from . models import contact
admin.site.register(contact)



class galleryAdmin(admin.ModelAdmin):
    list_display = ('pdes','gpic','gdate')

admin.site.register(gallery,galleryAdmin)

class eventsAdmin(admin.ModelAdmin):
    list_display = ('city','etitle','epurpose','epic','edate','sthanks')

admin.site.register(events,eventsAdmin)

class membershipAdmin(admin.ModelAdmin):
    list_display = ('name','dob','gender','email','mobile','city','profession','address','mdate')

admin.site.register(membership,membershipAdmin)



class donateAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','city','occupation','address','amount','ddate')

admin.site.register(donate,donateAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display = ('id','news','ndate')

admin.site.register(notification,notificationAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('cityname','cdate')

admin.site.register(city,cityAdmin)



class videoAdmin(admin.ModelAdmin):
    list_display=('id',"vtitle","vdes","thumb","vlink","vdate")
admin.site.register(video,videoAdmin)