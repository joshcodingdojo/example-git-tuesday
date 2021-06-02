from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  age = models.IntegerField()
  created_at = DateTimeField(auto_now=True)
  updated_at = DateTimeField(auto_now_add=True)