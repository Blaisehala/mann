from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
  user= models.OneToOneField(User, on_delete=models.CASCADE)
  image= models.ImageField(default='default.jpg')
  
  
  
  
class Project (models.Model):
  image = models.ForeignKey
  title = models.CharField(max_length=100, null=True, blank=True)

  description = models.TextField(max_length=300, null=True)
  user= models.ForeignKey(User, on_delete=models.CASCADE, default="" )
