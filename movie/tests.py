
from django.test import TestCase
from  .forms import MovieForm
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy, reverse
from .models import Movie, MovieGenre, MovieRating




class NewMovieForm(TestCase):
    def test_movieform(self):
        data = {{'moviename':'surface', 'moviecharacteristics': 'action', 'user': 'omar', 'entryDate': '2022-03-05', 'movieUrl' : 'https://testurl.com', 'moviedescription' : 'action and advanture'}} 
        form=MovieForm (data)
        self.assertTrue(form.is_valid )
    
    def test_MovieForm_Invalid(self):
        data = {{'moviename':'surface', 'moviecharacteristics': 'action', 'user': 'omar', 'entryDate': '2022-03-05', 'movieUrl' : 'https://testurl.com', 'moviedescription' : 'action and advanture'}} 
        form=MovieForm (data)
        self.assertFalse(form.is_valid )

# # Create your tests here.
# class ClubTest(TestCase):
#     def setUp(self):
#         self.type=Club(Clubname='C#')

#     def test_typestring(self):
#         self.assertEqual(str(self.type), 'C#')

#     def test_tablename(self):
#         self.assertEqual(str(Club._meta.db_table), 'Club')        

# class EventTest(TestCase):
#     def setUp(self):
#             self.type=Club(Clubname='C#')
#             self.user = User(username="user1")
#             self.event = Event(eventTitle = 'C#', eventUserId = self.user, eventDesc='C# Training', eventDate='02/22/2022', eventLocation='Bellevue')

#     def test_string(self):
#             self.assertEqual(str(self.event), 'C#')
    
#     def test_certificate(self):
#         cert = self.event.eventTitle
#         self.assertEqual(self.event.certificate(), cert)
    
# class NewEventForm(TestCase):
#     def test_eventform_is_valid(self):
#         data = {
#             {'eventtitle':'python', 'eventResource': 'python club', 'eventUserId': 'omurbek', 'eventDate':'2022-3-1', 'eventLocation': 'Seattle', 'eventDesc': 'Intro to python'}
#             } 
#         form=EventForm(data)
#         self.assertTrue(form.is_valid())

#     def test_Eventform_invalid(self):
#          data = {
#             {'eventtitle':'python', 'eventResource': 'python club', 'eventUserId': 'omurbek', 'eventDate':'2022-3-1', 'eventLocation': 'Seattle', 'eventDesc': 'Intro to python'}
#             } 
#         form=EventForm(data)
#         self.assertFalse(form.is_valid())
# class New_Event_Authentication_Test(TestCase):
#     def setUp(self):
#         self.test_user = User.objects.create_user(username = 'testuser1', password='P@assword1')
#         self.type=Type.object.create(typename='python')
#         self.event=Event.object.create(eventTitle = 'C#', eventUserId = self.test_user, eventDesc='C# Training', eventDate='02/22/2022', eventLocation='Bellevue') 

#     def test_redirect_if_not_logged_in(self):
#         response=self.client.get(reverse('newevent'))
#         self.assertRedirects(response, '/account/login/?next=/club/newevent/')   