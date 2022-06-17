from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Profile(models.Model):
  user= models.OneToOneField(User, on_delete=models.CASCADE)
  image= models.ImageField(default='default.jpg', upload_to='profile_pics')
  
  
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




class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )


    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    
    
    def save_rating(self):
        self.save()



    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings
    def __str__(self):
        return f'{self.project} Rating'