from django.shortcuts import render,request
from .models import Post
# Create your views here.
def new(request) :
    if request.method == 'POST' :
        title = request.POST.get('title')
        content = request.POST.get('content')
        post1 = Post(title=title,content=content)
        post1.save()
        return redirect('post:index')
    else :
        return render(request,'new.html')