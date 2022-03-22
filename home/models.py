from django.db import models
from django.utils import timezone

# Create your models here.

class Subscribe(models.Model):
  
    # email = models.EmailField(max_length=50)
    # date_submitted = models.DateTimeField(default=timezone.now)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

class UserData(models.Model):
  
    email = models.EmailField(max_length=50)
    name = models.TextField(max_length=50)