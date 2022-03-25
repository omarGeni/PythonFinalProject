from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('movies/', views.movies, name='movies'),
 path('movieDetail/<int:id>', views.movieDetail, name='detail'),
 path('newmovie/', views.newMovie, name='newmovie'),
]
