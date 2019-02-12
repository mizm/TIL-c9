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
    
def new(request,kind) :
    if request.method == "POST" :
        form = FoodForm(request.POST)
        if form.is_valid() :
            food = form.save(commit=False)
            food.kind = kind
            food.save()
            return redirect("article:index")
    else :
        form = FoodForm(initial={'kind': kind})
    return render(request,'form.html',{'form':form})
    
def index(request) :
    
    return render(request,'index.html')

def menu(request) :
    kind = request.POST.get('kind')
    foods = Food.objects.filter(kind=kind)
    return render(request,'menu.html',{'foods':foods, 'kind':kind})
    
def detail(request, food_id) :
    food = Food.objects.get(pk=food_id)
    return render(request,'detail.html',{'food':food})