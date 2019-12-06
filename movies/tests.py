from django.test import TestCase
import datetime

from movies.models import *
from movies.forms import *
from django.contrib.auth.models import User

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

class UserTests(TestCase):
    def setUp(self):
        u = User.objects.create_user('joe', 'lennon@thebeatles.com', 'johnpassword')
        
    def test1(self):
        User.objects.login(u)
        
    def test2(self):
        User.objects.logut(u)

class Review2Tests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Pika1")
        Movie.objects.create(title = "hi")
        user1 = User.objects.create_user('joe', 'lennon@thebeatles.com', 'johnpassword')
        user2 = User.objects.create_user('mike', 'mike@gmail.com', 'mikey')
        Review2.objects.create(id = "1", critic="Joe",
                              review="hello",
                              score = "8.7",
                              movie=Movie.objects.get(title="Pika1"),
                              user = user1,
                              review_type = True)
        Review2.objects.create(id = "2", critic="Mike",
                              review="what's up",
                              score = "2",
                              movie=Movie.objects.get(title="hi"),
                              user = user2,
                              review_type = True)
    def test1(self):
        review = Review2.objects.get(critic="Joe")
        self.assertEqual(review.critic, "Joe")
        self.assertEqual(review.review, "hello")
        self.assertEqual(review.movie.title, "Pika1")
        self.assertEqual(review.score , 8.7)
        self.assertEqual(review.user , User.objects.get(username = 'joe'))
        self.assertEqual(review.review_type , True)
        
    def test2(self):
        review = Review2.objects.get(critic="Joe")
        self.assertNotEqual(review.critic, "Joe2")
        self.assertNotEqual(review.review, "hello2")
        self.assertNotEqual(review.movie.title, "Pika12")
        self.assertNotEqual(review.score , 8.8)
        self.assertNotEqual(review.user , "x")
        self.assertNotEqual(review.review_type , False)
        
    def test3(self):
        review = Review2.objects.get(critic="Mike")
        self.assertNotEqual(review.critic, "Mike2")
        self.assertNotEqual(review.review, "hello2")
        self.assertNotEqual(review.movie.title, "Pika12")
        self.assertNotEqual(review.score , 8.8)
        self.assertNotEqual(review.user , "x")
        self.assertNotEqual(review.review_type , False)
        
    def test4(self):
        review = Review2.objects.get(critic="Mike")
        self.assertEqual(review.critic, "Mike")
        self.assertEqual(review.review, "what's up")
        self.assertEqual(review.movie.title, "hi")
        self.assertEqual(review.score , 2)
        self.assertEqual(review.user , User.objects.get(username = 'mike'))
        self.assertEqual(review.review_type , True)