from django import forms
from .models import Movie, MovieGenre, MovieRating

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields = '__all__'