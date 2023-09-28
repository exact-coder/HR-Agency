from django.contrib import admin
from .models import Registered_email
# Register your models here.

@admin.register(Registered_email)
class Registered_EmailAdmin(admin.ModelAdmin):
    list_display = ['id','email']
    list_display_links =['email']
    search_fields = ['email']
    list_per_page = 10
