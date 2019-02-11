from django.shortcuts import render,redirect
from .models import Food
from .forms import FoodForm
# # Create your views here.

# def new(request) :
#     if request.method == "POST" :
#         form = FoodModel(request.POST)
#         food = form.save()
#         return redirect("article:new")
#     else :
#         form = FoodModel()
    
#     return render(request,'form.html',{'form':form})
    
def new(request) :
    if request.method == "POST" :
        form = FoodForm(request.POST)
        food = form.save()
        return redirect("article:new")
    else :
        kind = request.GET.get('kind')
        form = FoodForm(initial={'kind': kind})
    return render(request,'form.html',{'form':form, 'kind':kind})
    
def index(request) :
    
    return render(request,'index.html')

def menu(request) :
    kind = request.GET.get('kind')
    foods = Food.objects.filter(kind=kind)
    return render(request,'menu.html',{'foods':foods, 'kind':kind})