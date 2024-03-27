from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

class User(AbstractUser):
    CREATOR='CREATOR'
    SUBSCRIBER='SUBSCRIBER'
    ROLE_CHOICE=(
        (CREATOR,'Créateur'),
        (SUBSCRIBER,'Abonné')
        )
    profile_photo=models.ImageField(verbose_name='Photo de profil')
    role=models.CharField(max_length=30,choices=ROLE_CHOICE,verbose_name='Rôle')
    follows=models.ManyToManyField('self',
        limit_choices_to={'role':CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )
    def givegroup(self):
        Group=apps.get_model('auth','Group')
        creators= Group.objects.get(name='creators')
        subscribers= Group.objects.get(name='subscribers')
        taskteam=Group.objects.get(name='taskteam')
        if self.role=='CREATOR':
            creators.user_set.add(self)
        if self.role=='SUBSCRIBER':
            subscribers.user_set.add(self)
        if 'taskmember' in self.username:
            taskteam.user_set.add(self)


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.givegroup()





