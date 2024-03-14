from django.db import models
from django.conf import settings
# Create your models here.
class Photo(models.Model):
    image=models.ImageField()
    caption=models.CharField(max_length=128,blank=True)
    uploader=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  f"{self.caption}"


class Blog(models.Model):
    photo=models.ForeignKey(Photo,null=True,on_delete=models.SET_NULL,blank=True)
    title=models.CharField(max_length=128)
    content=models.CharField(max_length=5000)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    def __str__(self):
        return  f"{self.title}"
