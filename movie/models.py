from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
# Each model will become a table in the database
class MovieGenre(models.Model):
    typename = models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='moviegenre'
    
class Movie(models.Model):
    moviename=models.CharField(max_length=255)
    moviecharacteristics=models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    entryDate=models.DateField()
    movieUrl=models.URLField()
    moviedescription=models.TextField()

    def __str__(self):
        return self.moviename
    
    class Meta:
        db_table='Movie'

class MovieRating(models.Model):
    ratingscale=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    ratingdate=models.DateTimeField()
    ratingText = models.TextField()
    

    def __str__(self):
        return self.ratingscale

    class Meta:
        db_table='movierating'