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
        Movie.objects.create(title="It's me",
                             director="Michael",
                             image= "hello.png",
                             star="you",
                             score="10",
                             runTime=13,
                             rating="PG",
                             releaseDate="2000-05-01",
                             studio="nbc",
                             link="mine")
    def setUp2(self):
        Movie.objects.create(title="It's me",
                             director="Michael",
                             image= "hello.png",
                             star="you",
                             score="10",
                             runTime=13,
                             rating="PG",
                             releaseDate="2000-05-01",
                             studio="nbc",
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

    def test3(self):
        movie = Movie.objects.get(title="It's me")

        self.assertEqual(movie.title, "It's me")
        self.assertEqual(movie.director, "Michael")
        self.assertEqual(movie.image, "hello.png")
        self.assertEqual(movie.star, "you")
        self.assertEqual(movie.score, 10)
        self.assertEqual(movie.runTime, 13)
        self.assertEqual(movie.rating, "PG")
        self.assertEqual(movie.releaseDate, datetime.date(2000, 5, 1))
        self.assertEqual(movie.studio, "nbc")
        self.assertEqual(movie.link, "mine")

    def test4(self):
        movie = Movie.objects.get(title="Hello World")

        self.assertNotEqual(movie.title, "It's me")
        self.assertNotEqual(movie.director, "Michael")
        self.assertNotEqual(movie.image, "x.png")
        self.assertNotEqual(movie.star, "you")
        self.assertNotEqual(movie.score, 10)
        self.assertNotEqual(movie.runTime, 13)
        self.assertNotEqual(movie.rating, "R")
        self.assertNotEqual(movie.releaseDate, datetime.date(2000, 5, 1))
        self.assertNotEqual(movie.studio, "nbc")
        self.assertNotEqual(movie.link, "to")


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
