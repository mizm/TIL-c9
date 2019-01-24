from django.shortcuts import render
import random
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')

# Template variable
def dinner(request):
    menu = ['김치볶음밥','족발','햄버거','치킨','초밥']
    pick = random.choice(menu)
    return render(request, 'dinner.html',{'dinner' : pick})

# Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name' : name})

    #container > div:nth-child(8) > script:nth-child(18)
def throw(request) :
    return render(request,'throw.html')

def catch(r):
    message = r.GET.get('message')
    return render(r,'catch.html', {'message' : message})

# Form 외부로 요청
def naver(request) :
    return render(request, 'naver.html')
# bootstrap
def bootstrap(request):
    return render(request,'bootstrap.html')