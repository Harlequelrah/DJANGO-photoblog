from django import forms
from django.contrib.auth import get_user_model
from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model=models.Photo
        fields=['image','caption']

class BlogForm(forms.ModelForm):
    # edit_blog=forms.BooleanField(initial=True,widget=forms.HiddenInput())
    class Meta:
        model=models.Blog
        fields=['title','content']

# class DeleteBlogForm(forms.ModelForm):
#     delete_blog=forms.BooleanField(initial=True,widget=forms.HiddenInput())
class NumberPhoto(forms.Form):
    number=forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 10}),required=False)
