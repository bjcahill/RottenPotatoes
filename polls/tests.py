from django.test import TestCase
from polls.models import *

class MoviesTests(TestCase):
    def setUp(self):
        Movie.objects.create(title="Hello World")

    def test1(self):
        movie = Movie.objects.get(title="Hello World")

        self.assertEqual(movie.getTitle(), "Hello World")

    def test2(self):
        movie = Movie.objects.get(director="Mike Ford")

        self.assertEqual(movie.getDirector(), "Mike Ford")

   
    def test3(self):
        movie = Movie.objects.get(score="10")

        self.assertEqual(movie.getScore(), "10")


    def test4(self):
        movie = Movie.objects.get(star="Hello World")

        self.assertEqual(movie.getStar(), "4")
    
    def test5(self):
        movie = Movie.objects.get(runTime="60")

        self.assertEqual(movie.getRunTime(), "60")
class ReviewTests(TestCase):
    def setUp(self):
        Review.objects.create(critic="Joe", movie=Movie.objects.get(title="Pika1"))

    def test1(self):
        review = Review.objects.get(critic="Joe")

        self.assertEqual(review.getCritic(), "Joe")
