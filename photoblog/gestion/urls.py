from django.urls import path,include
from . views import *
urlpatterns = [
    path('get-tasks/<str:id>/',display_tasks,name='get_tasks'),
    path('post-task',post_task,name='post_task'),
    path('change-task/<str:id>/',change_task,name='change_task'),


]
