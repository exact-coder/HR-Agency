from django.contrib import admin
from .models import Registered_email,Support,Message
from django.utils.html import format_html
# Register your models here.

@admin.register(Registered_email)
class Registered_EmailAdmin(admin.ModelAdmin):
    list_display = ['id','email']
    list_display_links =['email']
    search_fields = ['email']
    list_per_page = 10

# SUPPORT
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = ['person','email','option','created_at','status','_']
    search_fields = ['persion','option']
    list_per_page = 10

    # Function to change the icons (Done - Pending)
    def _(self,obj):
        if obj.Situation == 'Done':
            return True
        else:
            return False
    _.boolean = True

    # Function to color the text (Done - Pending)
    def status(self,obj):
        if obj.Situation == 'Done':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))
    status.allow_tags = True

# MESSAGE

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = ['id','email','text','status','_']
    list_display_links = ['id','email']
    list_per_page = 10
    # Function to change the icons (Done - Pending)
    def _(self,obj):
        if obj.Situation == 'Read':
            return True
        else:
            return False
    _.boolean = True

    # Function to color the text (Done - Pending)
    def status(self,obj):
        if obj.Situation == 'Read':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))
    status.allow_tags = True

