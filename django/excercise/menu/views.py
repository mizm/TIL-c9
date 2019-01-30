from django.shortcuts import render,redirect
from .models import Question,Choice
# Create your views here.
def index(request) :
    questions = Question.objects.last()
    return render(request, 'index2.html', {'questions' : questions})

def select(request) :
    choice_id = request.GET.get('menu_list')
    print(choice_id)
    choice = Choice.objects.get(pk=int(choice_id))
    choice.votes = choice.votes + 1
    choice.save()
    return redirect('menu:index')