from django.contrib import admin
from .models import Movie, MovieGenre, MovieRating

# Register your models here.
# Necessary if they are to appear in the admin
admin.site.register(Movie)
admin.site.register(MovieGenre)
admin.site.register(MovieRating)
