from turtle import title
from django.test import TestCase
from .models import Profile,Project, Rating

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
    self.jiji = Profile(image='http//')
  def test_instance(self):
    self.assertTrue(isinstance(self.jiji,Profile))






class ProjectleTestClass(TestCase):
  def setUp(self):
    self.first = Project(image='http',title='hey', description='hello')
  def test_instance(self):
    self.assertTrue(isinstance(self.first,Project))


class RatingleTestClass(TestCase):
  def setUp(self):
    self.two = Rating(design='1', usability='1', content='1')
  def test_instance(self):
    self.assertTrue(isinstance(self.two,Rating))


