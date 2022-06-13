from django.db import models

# Create your models here.


class Posts (models.Model):
  image = models.ForeignKey
  title = models.CharField(max_length=100, null=True, blank=True)
  # post  = HTMLField(max_length=)
  description = models.TextField(max_length=300, null=True)
