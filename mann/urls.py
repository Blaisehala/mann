from django.urls import path
from . import views


# from .views import AddPostView

urlpatterns = [

    path('', views.landing, name='mann-landing'),
    path('home/', views.home, name='mann-home'),
    path('about/', views.about, name='mann-about'),
    path ('newpost/',views.new_post, name='newpost'),
    path ('rate/<int:id>',views.rate, name='rate'),
    path ('home/api/profile/',views.ProfileList.as_view(), name=''),
    path ('home/api/project/',views.ProjectList.as_view(), name=''),
    
       
]