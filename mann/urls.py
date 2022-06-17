from django.urls import path
from . import views


# from .views import AddPostView

urlpatterns = [

    # path('', views.landing, name='mann-landing'),
    path('', views.home, name='mann-home'),
    path('about/', views.about, name='mann-about'),
    path ('newpost/',views.new_post, name='newpost'),
    path ('project/<int:id>',views.project, name='project'),
    path ('api/profile/',views.ProfileList.as_view(), name=''),
    path ('api/project/',views.ProjectList.as_view(), name=''),
    
       
]