from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.
def index(request) :
    movies = Movie.objects.all()
    return render(request,'movie.html',{'movies':movies})
    
def new_movie(request) :
    return render(request,'new_movie.html')

def create_movie(request) :
    title_kr = request.POST.get('title_kr')
    title_en = request.POST.get('title_en')
    spectators = request.POST.get('spectators')
    summary = request.POST.get('summary')
    info_url = request.POST.get('info_url')
    score = request.POST.get('score')
    genre = request.POST.get('genre')
    poster = request.FILES.get('poster')
    picture1 = request.FILES.get('picture1')
    picture2 = request.FILES.get('picture2')
    picture3 = request.FILES.get('picture3')
    movie = Movie(title_kr=title_kr,title_en=title_en,spectators = spectators, summary=summary, info_url = info_url, score = score, genre=genre, poster=poster,picture1 = picture1, picture2 = picture2, picture3 = picture3)
    movie.save()
    return redirect('files:index')