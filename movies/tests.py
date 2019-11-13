from django.test import TestCase
import datetime

from movies.models import *
from movies.forms import *

class MoviesTests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Hello World",
                             director="Mike Ford",
                             image= "hello.png",
                             star="me",
                             score="8.7",
                             runTime=120,
                             rating="PG",
                             releaseDate="2000-01-01",
                             studio="abc",
                             link="mine")

    def test1(self):
        movie = Movie.objects.get(title="Hello World")

        self.assertEqual(movie.title, "Hello World")
        self.assertEqual(movie.director, "Mike Ford")
        self.assertEqual(movie.image, "hello.png")
        self.assertEqual(movie.star, "me")
        self.assertEqual(movie.score, 8.7)
        self.assertEqual(movie.runTime, 120)
        self.assertEqual(movie.rating, "PG")
        self.assertEqual(movie.releaseDate, datetime.date(2000, 1, 1))
        self.assertEqual(movie.studio, "abc")
        self.assertEqual(movie.link, "mine")

    def test2(self):
        form = TestMovieForm({'title': "Testing"})
        self.assertTrue(form.is_valid())

class ReviewTests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Pika1")
        Review.objects.create(critic="Joe",
                              review="hello",
                              movie=Movie.objects.get(title="Pika1"))

    def test1(self):
        review = Review.objects.get(critic="Joe")

        self.assertEqual(review.critic, "Joe")
        self.assertEqual(review.review, "hello")
        self.assertEqual(review.movie.title, "Pika1")
