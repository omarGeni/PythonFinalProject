
from django.test import TestCase
from  .forms import MovieForm
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy, reverse
from .models import Movie, MovieGenre, MovieRating


# # Create your tests here.
class MovieTest(TestCase):
    def setUp(self):
        self.type=Movie(Clubname='Friends')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Friends')

    def test_tablename(self):
        self.assertEqual(str(Movie._meta.db_table), 'Movie')        

class MovieRating(TestCase):
    def setUp(self):
            self.type=Movie(Clubname='Friends')
            self.user = User(username="user1")
            self.event = MovieRating(ratingscale = 'iMBD', user = self.test_user, ratingText='Friends', ratingdate='02/22/2022')

    def test_string(self):
            self.assertEqual(str(self.event), 'Friends')
    

class NewMovieForm(TestCase):
    def test_movieform(self):
        data = {{'moviename':'surface', 'moviecharacteristics': 'action', 'user': 'omar', 'entryDate': '2022-03-05', 'movieUrl' : 'https://testurl.com', 'moviedescription' : 'action and advanture'}} 
        form=MovieForm (data)
        self.assertTrue(form.is_valid )
    
    def test_MovieForm_Invalid(self):
        data = {{'moviename':'surface', 'moviecharacteristics': 'action', 'user': 'omar', 'entryDate': '2022-03-05', 'movieUrl' : 'https://testurl.com', 'moviedescription' : 'action and advanture'}} 
        form=MovieForm (data)
        self.assertFalse(form.is_valid )

class New_Movie_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password='P@assword2')
        self.type=Movie.object.create(typename='Friends')
        self.event=MovieRating.object.create(ratingscale = 'iMBD', user = self.test_user, ratingText='Friends', ratingdate='02/22/2022') 

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/account/login/?next=/movie/newmovie/')   