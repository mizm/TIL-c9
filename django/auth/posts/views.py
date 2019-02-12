from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

#def throw
#def catch
#decorators @ 파라미터로 함수를 받음
#login_required의 기본 전달 url은 '/accounts/login/'
@login_required
def new(request) :
    if request.method == 'POST' :
        #create
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        post = Post(title=title,content=content,image=image)
        post.save()
        return redirect('posts:detail',post.pk)
    else :
        # new
        return render(request,'new.html')

def index(request):
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts' : posts})

def detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    c = post.comment_set.all()
    return render(request,'detail.html', {'post' : post,'comments':c})
    
def naver(request,q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
def delete(request, post_id) :
    if request.method == 'POST' :
        #delete
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    else :
        return render(request,'delete.html')                                            

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST' :
        #update
        title=request.POST.get('title')
        content=request.POST.get('content')
        post = Post.objects.get(pk=post_id)
        post.title = title
        post.content = content
        post.save()
        return redirect('posts:detail',post.pk)
    else :
        return render(request, 'edit.html', {'post' : post})

def comments_create(request,post_id) :
    post = Post.objects.get(pk=post_id)
    content = request.POST.get('content')
    c = Comment(post=post,content=content)
    c.save()
    return redirect('posts:detail',post_id)

def comments_delete(request,post_id,comment_id) :
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail',post_id)