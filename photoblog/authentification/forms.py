from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User=get_user_model()
class LoginForm(forms.Form):
    username=forms.CharField(max_length=63,label="Nom d' utilisateur ")
    password=forms.CharField(max_length=63,widget=forms.PasswordInput(),label='Mot de passe')


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=get_user_model()
        fields=('username','email','first_name','last_name','role')

class UserPPForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['profile_photo']
# from . import validators
# class PostCodeForm(forms.Form):
#     post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['follows']
