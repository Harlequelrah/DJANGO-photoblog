from django.contrib import admin

# Register your models here.
from . import models
class BlogAdmin(admin.ModelAdmin):
    # list_display=('title','author','date_created')
    list_display=('title','date_created')

class PhotoAdmin(admin.ModelAdmin):
    list_display=('caption','uploader','date_created')

admin.site.register(models.Blog,BlogAdmin)
admin.site.register(models.Photo,PhotoAdmin)
