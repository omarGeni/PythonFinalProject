from django.shortcuts import render
from .models import Movie, MovieGenre, MovieRating
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import MovieForm

# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'movie/movies.html', {'movie.list': movie_list})

def movieDetail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movie/moviedetail.html', {'movie': movie})

def newMovie(request):
    form=MovieForm

    if request.method =='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MovieForm()
        else: 
            form = MovieForm()
        
        return render(request, 'movie/newmovie.html', {'form': form})

@login_required
def newMovie(request):
    form=MovieForm

    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=MovieForm()
    else:
        form=MovieForm()
    return render(request, 'reviews/newreview.html', {'form': form})

def logoutmessage(request):
    return render(request, 'reviews/logoutmessage.html')

def loginmessage(request):
    return render(request, 'reviews/loginmessage.html')