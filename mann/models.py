from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
  user= models.OneToOneField(User, on_delete=models.CASCADE)
  image= CloudinaryField('image',default='default.jpg')
  
  
  def __str__(self):
    return f'{self.user.username} profile'


  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)

  def delete_profile(self):
    self.delete()




class Project (models.Model):
  title = models.CharField(max_length=100, null=True, blank=True)
  image = CloudinaryField('image', default='default.jpg')
  link = models.URLField(null=True, blank=True)
  description = RichTextField(null=True, blank=True)
  created = models.DateTimeField(auto_now=True)
  user= models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self): 
    return self.title


  def save_project(self):
    self.save()


  def delete_project(self):
    self.delete()





class vote(models.Model):
   project = models.ForeignKey(Project, on_delete=models.DO_NOTHING,null=True)
   choice_text = models.CharField(max_length=200, null=True)
   your_vote = models.IntegerField(max_length=20)