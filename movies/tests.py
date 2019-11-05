from django.test import TestCase

from polls.models import *
from polls.forms import *

class MoviesTests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Hello World", director="Mike Ford", score="8.7")

    def test1(self):
        movie = Movie.objects.get(title="Hello World")

        self.assertEqual(movie.getTitle(), "Hello World")
        self.assertEqual(movie.getDirector(), "Mike Ford")
        self.assertEqual(movie.getScore(), 8.7)

    def test2(self):
        form = TestMovieForm({'title': "Testing"})
        self.assertTrue(form.is_valid())


class ReviewTests(TestCase):
    def setUp(self):
        Review.objects.create(critic="Joe", movie=Movie.objects.get(title="Pika1"))

    def test1(self):
        review = Review.objects.get(critic="Joe")
        self.assertEqual(review.getCritic(), "Joe")

