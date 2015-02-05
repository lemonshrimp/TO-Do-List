from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here

class To_do(models.Model): 
  user = models.ForeignKey(User)
  Title = models.CharField(max_length=150, unique=True)
  Content = models.TextField(max_length=250)
  Date =  models.DateTimeField(default=datetime.datetime.now)
  isCompleted = models.BooleanField(default=False) 
  inList = models.ForeignKey(tdList)
  
  def __str__(self):
      return self.title

  class Meta:
    ordering = ['Date', 'Title']
  
  class Admin:
    pass
  
class tdList(models.Model):
  
  Title = models.CharField(max_length=150, unique=True)
  #User = model.ForeignKey(Users)
  def __str__(self):
      return self.title
      
  class Meta:
    ordering = ['Title']
  
  class Admin:
    pass
  


  
  
