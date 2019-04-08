from django.shortcuts import render,redirect
from .models import post

# Create your views here.

def index(request) :
    posts = post.objects.all()
    return render(request,'index.html', {'posts' : posts})
    
def detail(request,post_id) :
    post1 = post.objects.get(pk=post_id)
    return render(request,'detail.html',{'post':post1})
def delete(request,post_id) :
    post1 = post.objects.get(pk=post_id)
    post1.delete()
    return redirect('post:index')
def new(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        post1 = post(title=title,content=content)
        post1.save()
        return redirect('post:index')
    else :
        return render(request,'new.html')