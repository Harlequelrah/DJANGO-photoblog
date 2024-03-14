from django.urls import path,include
from . views import *
urlpatterns = [
    path('home/',home,name='home'),
    path('photo/upload/',photo_upload,name='photo_upload'),
    path('create/blog',blog_and_photo_upload,name='blog_create'),
    path('<int:blog_id>',view_blog,name='view_blog'),


]
