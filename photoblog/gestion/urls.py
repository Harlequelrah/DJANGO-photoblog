from django.urls import path,include
from . views import *
urlpatterns = [
    path('get-tasks/',display_tasks,name='get_tasks'),


]
