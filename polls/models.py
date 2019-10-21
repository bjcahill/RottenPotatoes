from django.db import models
import psycopg2

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="/images/pika.jpeg")

    def __str__(self):
        return self.title
