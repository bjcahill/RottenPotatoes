from django.db import models
from django.template.defaultfilters import slugify
import psycopg2

# Create your models here.
class Usermodel(models.Model):
   user_name = models.CharField(max_length = 100,default="NULL")
   first_name = models.CharField(max_length = 100,default="NULL")
   last_name = models.CharField(max_length = 100,default="NULL")
   average_rating = models.FloatField(default = 0)
   join_date = models.DateTimeField('date joined')
   user = models.ForeignKey('auth.User', default=1, on_delete=models.SET_DEFAULT)
   image = models.ImageField(upload_to='images', blank=True)

   def __str__(self):
      return self.user_name