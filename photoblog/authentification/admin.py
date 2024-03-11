from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    liste_display=('username','email','role')
admin.site.register(User,UserAdmin)
