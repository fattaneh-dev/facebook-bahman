from email import message

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from core.models import User, Post
from core.forms import NewPostForm


def say_hello(request): #view function
    return HttpResponse('<h1 style="color: red; text-align:center;">Hello world!</h1>')

def home(request, username):
    name = User.objects.filter(username=username).first()
    context = {
        'first_name': name.name.capitalize() if name else 'World'
    }
    return render(request, 'core/index.html', context=context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'core/post_list.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post':post
    }
    return render(request, 'core/post_detail.html', context=context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'پست شما با موفقیت حذف شد')
    return redirect('post_list')


def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            title = form.validated_data.get('title')
            content = form.validated_data.get('content')
            user = form.validated_data.get('user')
            image = form.validated_data.get('image')
            new_post = Post.objects.create(title=title, content=content, user=user,image=image)
            messages.success(request, 'پست شما با موفقیت ساخته شد')
            return redirect('post_list')
        
    form = NewPostForm()
    context = {
        'form':form
    }
    return render(request, 'core/new_post.html', context=context)