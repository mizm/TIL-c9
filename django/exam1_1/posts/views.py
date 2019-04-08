from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def new(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        post1 = Post(title=title,content=content)
        post1.save()
        return redirect('posts:index')
    else :
        return render(request,'new.html')
        
def index(request) :
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def detail(request,post_id) :
    post = Post.objects.get(pk=post_id)
    return render(request,'detail.html',{'post':post})

def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:index')