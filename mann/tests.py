from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestClass(TestCase):
  def setUp(self):
    
    self.jiji = Profile(image='http')
  def test_instance(self):
    self.assertTrue(isinstance(self.jiji,Profile))