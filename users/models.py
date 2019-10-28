from django.db import models

# Create your models here.
class Usermodel(models.Model):
   user_name = models.CharField(max_length = 100)
   join_date = models.DateTimeField('date joined')

   def __str__(self):
      return self.user_name