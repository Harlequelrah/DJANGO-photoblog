from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR='CREATOR'
    SUBSCRIBER='SUBSCRIBER'
    ROLE_CHOICE=(
        (CREATOR,'Créateur'),
        (SUBSCRIBER,'Abonné')
        )
    profile_photo=models.ImageField(verbose_name='Photo de profil')
    role=models.CharField(max_length=30,choices=ROLE_CHOICE,verbose_name='Rôle')



