from django.test import TestCase
from polls.models import *

class MoviesTests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Hello World")

    def test1(self):
        movie = Movie.objects.get(title="Hello World")

        self.assertEqual(movie.getTitle(), "Hello World")

class ReviewTests(TestCase):
    def setUp(self):
        Review.objects.create(critic="Joe", movie=Movie.objects.get(title="Pika1"))

    def test1(self):
        review = Review.objects.get(critic="Joe")

        self.assertEqual(review.getCritic(), "Joe")
