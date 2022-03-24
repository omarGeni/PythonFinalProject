from django.shortcuts import render
from .models import Movie, MovieGenre, MovieRating
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'movie/index.html')

def movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'movie/movies.html', {'movie.list': movie_list})