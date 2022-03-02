from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from app_example.models import Movie

# Create your tests here.

class MovieTester(TestCase):

  # setup sample data for testing
  def setUp(self):
    self.user = get_user_model().objects.create(
      username='tester', email='tester@email.com', password='pass'
    )
    self.movie = Movie.objects.create(
      name = 'Dune', rating = 8, reviewer = self.user
    )

  
  def test_string_rep(self):
    self.assertEqual(str(self.movie), 'Dune')