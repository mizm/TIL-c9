from django.shortcuts import render,redirect
from .models import Student
from .models import Post
# Create your views here.
def index(request) :
    students = Student.objects.all()
    tempposts = Post.objects.all()
    posts = []
    for post in tempposts :
        temp = {}
        temp['RK'] = tempposts.RK
        temp['name'] = Student.objects.get(pk=post.RK).name
        temp['message'] = post.message
        posts.append(temp)

    return render(request,'index.html',{'students':students,'posts':posts})

def new(request):
    return render(request,'new.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    student = Student(name=name,email=email,birthday=birthday,age=age)
    student.save()
    return redirect(f'/posts/{student.pk}')

def detail(request,st_id) :
    student = Student.objects.get(pk=st_id)
    return render(request,'detail.html',{'student':student})
    
def delete(request,st_id) :
    student = Student.objects.get(pk=st_id)
    student.delete()
    return redirect('/posts/')
    
def edit(request,st_id) :
    student = Student.objects.get(pk=st_id)
    return render(request,'edit.html',{'student':student})
    
def update(request,st_id) :
    st = Student.objects.get(pk=st_id)
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    st.name = name
    st.email = email
    st.birthday = birthday
    st.age = age
    st.save()
    return redirect(f'/posts/{st.pk}')

def search(request) :
    name = request.GET.get('name')
    students = Student.objects.filter(name=name).all()
    return render(request,'search.html',{'students' : students})

def write(request,st_id) :
    st = Student.objects.get(pk=st_id)
    return render(request,'write.html',{'st':st})
    
def send(request,rk) :
    message = request.POST.get('message')
    s = Post(RK=rk,message=message)
    s.save()
    return redirect('/posts/')
    