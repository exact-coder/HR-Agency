from django.contrib import admin
from .models import Registered_email,Support,Message,Notepad,Vacancies,Countdown,Waiting
from django.utils.html import format_html
# Register your models here.

@admin.register(Registered_email)
class Registered_EmailAdmin(admin.ModelAdmin):
    list_display = ['id','email']
    list_display_links =['email']
    search_fields = ['email']
    readonly_fields = ['email']
    list_per_page = 10

# SUPPORT
@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = ['person','email','option','created_at','status','_']
    search_fields = ['persion','option']
    readonly_fields = ('person','email','option','created_at','message')
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
    readonly_fields = ('id','email','text')
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

# Notepad
@admin.register(Notepad)
class NotepadAdmin(admin.ModelAdmin):
    list_display = ['id','title','text']
    list_display_links = ['title']

# Vacancies
@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ['id','frontend','backend','fullstack','intern']

# Countdown
@admin.register(Countdown)
class CountdownAdmin(admin.ModelAdmin):
    list_display = ['id','timer']

# Waiting
@admin.register(Waiting)
class WaitingAdmin(admin.ModelAdmin):
    list_filter=['Situation','job']
    list_display = ['id','job','email','message','Situation','company_note']
    list_display_links=['id','job']
    readonly_fields = ('id','job','email','message','profile_document')
    search_fields=['job']
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

