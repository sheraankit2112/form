from django.contrib import admin

# Register your models here.
from my.models import userdata

class UserAdmin(admin.ModelAdmin):
    list_display=["name","age","email"]

admin.site.register(userdata,UserAdmin)
