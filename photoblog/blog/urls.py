from django.urls import path,include
from . views import *
urlpatterns = [
    path('home/',home,name='home'),
]
