from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
# Create your views here.

def logout_page(request):
    logout(request)
    return redirect('login')


def mailtrap(request, email):
    message = EmailMessage(
        subject=f"Message from {email} Via FotoBlog",
        body="Voici le lien de reinitialisation de votre mot de passe, <a href='http://localhost:8000/change-password/'>Changer le mot de passe</a>",
        from_email=email,
        to=['FotoBlog@gmail.com'],
        )
    message.content_subtype = "html"  # Set content type to HTML
    message.send()
    messages.success(request,'Veuillez consulter votre boite mail pour obtenir le lien de reinitialisation de votre mot de passe')
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = 'authentification/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Vous êtes connecté avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Identifiants invalides.')
        return super().form_invalid(form)


def signup_page(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            # return redirect('home')
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,'authentification/signup.html',context={'form':form})




@login_required
def photo_update(request):
    form=UserPPForm(instance=request.user)
    if request.method=='POST':
        form=UserPPForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            photo=form.save()
            # photo=form.save(commit=False)
            # photo.save()
            # request.user.profile_photo=photo
            # request.user.save()
            return redirect('home')
    return render(request,'blog/photo_profile_update.html',context={'form':form})



# class LoginPageView(View,LoginRequiredMixin):
#     template_name='authentification/login.html'
#     form_class=LoginForm
#     def get(self,request):
#         form=self.form_class()
#         render (request,'authentification/login.html',context={'form':form})
#     def post(self,request):
#         form=self.form_class()
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request,user)
#                 message=f'Bonjour , {user.username}! Vous êtes connecté .'
#                 messages.success(request,message)
#                 return redirect('home')

#             else:
#                 messages.error(request,'Identifiants invalides')
#                 return redirect('login')
#         return render (request,'authentification/login.html',context={'form':form})

# def login_page(request):
#     form=LoginForm()
#     message=''
#     if request.method == 'POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request,user)
#                 message=f'Bonjour , {user.username}! Vous êtes connecté .'
#                 messages.success(request,message)
#                 return redirect('home')

#             else:
#                 messages.error(request,'Identifiants invalides')
#                 return redirect('login')
#     return render (request,'authentification/login.html',context={'form':form})

