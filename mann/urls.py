from django.urls import path
from . import views


# from .views import AddPostView

urlpatterns = [
    path('', views.home, name='mann-home'),
    path('about/', views.about, name='mann-about'),
    
    
     
]