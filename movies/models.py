from django.db import models
from django.template.defaultfilters import slugify
import psycopg2

# Create your models here.
class Movie(models.Model):
    RATING_CHOICES = [
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17'),
    ]

    title = models.CharField(max_length=100, default="NULL", primary_key=True)
    director = models.CharField(max_length=100, default="NULL")
    image = models.ImageField(upload_to='images', blank=True, default="omegalul.png")
    star = models.CharField(max_length=100, default="NULL")
    runTime = models.IntegerField(default=0)
    rating = models.CharField(max_length=5,
                              choices=RATING_CHOICES,
                              default='G')
    releaseDate = models.DateField(default='1900-01-01')
    studio = models.CharField(max_length=100, default="NULL")
    link = models.SlugField(max_length=100, default="NULL")

    score = models.FloatField(default=0)
    reviews = models.FloatField(default=0)
    aggScore = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
    critic = models.CharField(max_length=50, default="NULL", primary_key=True)
    review = models.TextField(max_length=1000, default="NULL")
    movie = models.ForeignKey(Movie, default=1, on_delete=models.SET_DEFAULT)

class Review2(models.Model):
    id = models.AutoField(primary_key=True)
    critic = models.CharField(max_length=50, default="NULL")
    review = models.TextField(max_length=1000, default="NULL")
    score = models.FloatField(default=0)
    movie = models.ForeignKey(Movie, default=1, on_delete=models.SET_DEFAULT)

class UserReview(models.Model):
    critic = models.CharField(max_length=50, default="NULL", primary_key=True)
    review = models.TextField(max_length=1000, default="NULL")
    movie = models.ForeignKey(Movie, default=1, on_delete=models.SET_DEFAULT)
