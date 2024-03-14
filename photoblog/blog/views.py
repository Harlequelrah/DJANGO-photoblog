from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
# Create your views here.
from . import forms,models
@login_required
def home(request):
    photos=models.Photo.objects.all()
    blogs=models.Blog.objects.all()
    return render(request,"blog/home.html",context={'photos':photos,'blogs':blogs})

@login_required
def photo_upload(request):
    form=forms.PhotoForm()
    if request.method=='POST':
        form=forms.PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.uploader=request.user
            photo.save()
            messages.success(request,"Votre photo a été uploadée avec succès")
            return redirect('home')
    return render(request,'blog/photo_upload.html',context={'form':form})

@login_required
def blog_and_photo_upload(request):
    blog_form=forms.BlogForm()
    photo_form=forms.PhotoForm()
    if request.method=='POST':
        blog_form=forms.BlogForm(request.POST)
        photo_form=forms.PhotoForm(request.POST,request.FILES)
        if all([photo_form.is_valid() ,blog_form.is_valid()]):
            photo=photo_form.save(commit=False)
            photo.uploader=request.user
            photo.save()
            blog=blog_form.save(commit=False)
            blog.author=request.user
            blog.photo=photo
            blog.save()
            messages.success(request,"Votre billet a été enreistré avec succès")
            return redirect('home')
    context={
        'blog_form':blog_form,
        'photo_form':photo_form
    }
    return render(request,'blog/create_blog_post.html',context=context)



@login_required
def view_blog(request,blog_id):
    blog=get_object_or_404(models.Blog,id=blog_id)
    return render(request,'blog/view_blog.html',context={'blog':blog})
