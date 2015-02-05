from django.db import models
import datetime

# Create your models here

class To_do(models.Model): 

  Title = models.CharField(max_length=150, unique=True)
  Content = models.TextField(max_length=250)
  Date =  models.DateTimeField(default=datetime.datetime.now)
  def __str__(self):
      return self.title

  class Meta:
    ordering = ['Date', 'Title']
  
  class Admin:
    pass
  
  
