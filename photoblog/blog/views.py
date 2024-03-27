from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required
from django.conf import settings
from django.forms import formset_factory
from django.contrib import messages
# Create your views here.
from . import forms,models
from django.db.models import Q
from itertools import chain



@login_required
@permission_required(['blog.view_photo','blog.view_blog'],raise_exception=True)
def home(request):
    # Photo.objects.filter(blog__contributors__first_name='Peter')
    # photos=models.Photo.objects.all()
    # blogs=models.Blog.objects.all()
    # blogs = blogs.order_by('-date_created') inverser l ordre des sequences
    blogs=models.Blog.objects.filter(
        Q(contributors__in=request.user.follows.all()) |
        Q(starred=True)|
        Q(contributors=request.user)
    )
    photos=models.Photo.objects.filter(
        Q(uploader__in=request.user.follows.all()) |
        Q(uploader=request.user)
    ).exclude(
            blog__in=blogs
        )

    blogs_and_photos=sorted(

        chain(blogs,photos),
        key= lambda instance:instance.date_created,
        reverse=True
    )
    return render(request,"blog/home.html",context={'blogs_and_photos':blogs_and_photos})
    # return render(request,"blog/home.html",context={'photos':photos,'blogs':blogs})

@login_required
@permission_required('blog.view_photo',raise_exception=True)
def photo_feed(request):
    photos=models.Photo.objects.filter(
        uploader__in=request.user.follows.all()
    ).order_by('-date_created')
    return render(request,'blog/photo_feed.html',context={"photos":photos})



@login_required
@permission_required('blog.add_photo',raise_exception=True)
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
@permission_required(['blog.add_photo','blog.add_blog'],raise_exception=True)
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
            blog.contributors.add(request.user,through_defaults={'contribution':'Acteur principale'})
            messages.success(request,"Votre billet a été enreistré avec succès")
            return redirect('home')
    context={
        'blog_form':blog_form,
        'photo_form':photo_form
    }
    return render(request,'blog/create_blog_post.html',context=context)





@login_required
@permission_required('blog.view_blog',raise_exception=True)
def view_blog(request,blog_id):
    blog=get_object_or_404(models.Blog,id=blog_id)
    return render(request,'blog/view_blog.html',context={'blog':blog})

@login_required
@permission_required('blog.change_blog',raise_exception=True)
def edit_blog(request,blog_id):
    blog=get_object_or_404(models.Blog,id=blog_id)
    edit_form=forms.BlogForm(instance=blog)
    # delete_form=forms.DeleteBlogForm()
    if request.method=='POST':
        if 'edit_blog' in request.POST:
            edit_form=forms.BlogForm(request.POST,instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request,'Votre blog a été modifié avec succès')
                return redirect('home')
        elif 'delete_blog' in request.POST:
            # delete_from=forms.DeleteBlogForm(request.POST)
            # if delete_form.is_valid():
                blog.delete()
                messages.success(request,'Votre blog a été supprimé avec succès')
                return redirect('home')
    context={
        'edit_form':edit_form,
        # 'deleted_form':delete_form,
    }
    return render(request,'blog/edit_blog.html',context=context)

@login_required
@permission_required('blog.add_photo',raise_exception=True)
def upload_multiple_photo(request,number):
    numberform=forms.NumberPhoto()
    if request.method=='POST' and 'num' in request.POST:
        numberform=forms.NumberPhoto(request.POST)
        if numberform.is_valid():
            number=numberform.cleaned_data['number']
    PhotoFormset=formset_factory(forms.PhotoForm,extra=number)
    formset=PhotoFormset()
    if request.method == 'POST' and 'submit' in request.POST:
        formset=PhotoFormset(request.POST,request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo=form.save(commit=False)
                    photo.uploader=request.user
                    photo.save()
            return redirect('home')
    return render(request,'blog/upload_multiple_photo.html',context={'formset':formset,'numberform':numberform})







