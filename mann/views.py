from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,NewProjectForm, RatingForm
from mann.models import Project
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Project,Profile
from .serializer import ProfileSerializer,ProjectSerializer
from .models import *
from django.http import  HttpResponseRedirect




# Create your views here.


# def landing(request):
  
#   return render(request, 'users/landing.html', )


def rate(request):
  
  return render(request, 'users/rate.html', )

def home(request):
  project = Project.objects.all()

  # context= {
  #   'projects': Project.objects.all()
  # }
  

  return render(request, 'users/home.html',{'project':project})


# about view
def about(request):
  return render(request, 'users/about.html', {'title': 'About'})



def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}.You can Login')
      return redirect ('login')
      
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})
 



@login_required
def profile(request): 
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
    current_user=request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    
    if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request, f'Account updated succefully.')
       return redirect('profile')

  else:
     u_form = UserUpdateForm(instance=request.user)
     p_form = ProfileUpdateForm(instance=request.user.profile)


  context = {
    'u_form': u_form,
    'p_form': p_form,
    
  }
  

  return render(request, 'users/profile.html', context)


class AddPostView(CreateView):
  model: Project
  template_name = 'users/home.html'
  fields =['title', 'description', 'image','link']


  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


@login_required(login_url='/users/login')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form =NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      print('post')
      project = form.save(commit=False)
      
      project.user = current_user
      project.save()
    return redirect('mann-home')
  
  else:
    form = NewProjectForm()

  return render(request, 'users/newpost.html', {'form':form})



# @login_required(login_url='login')
# def rate(request, id):

#     # form = RateProjectForm()
#     project = Project.objects.get(id=id)
    
#     context = {
#         'project': project,
#         # 'form': form
#     }
#     return render(request, 'users/rate.html', context)




class ProjectList(APIView):
  def get(self, request, format=None):
    all_project = Project.objects.all()
    serializers = ProjectSerializer(all_project, many=True)
    return Response(serializers.data)


class ProfileList(APIView):
  def get(self, request, format=None):
    all_profile = Profile.objects.all()
    serializers = ProfileSerializer(all_profile, many=True)
    return Response(serializers.data)




@login_required
def project(request,id):
    form = RatingForm()
    project = Project.objects.filter(id=id).first()
    ratings = Rating.objects.filter(user=request.user,id=id).first()
    rating_status = None
    if rating_status is None:
        rating_status = False
    else:
        rating_status = True    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rating.objects.filter(project=project)
            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)
            usability_ratings = [us.usability for us in project_ratings] 
            usability_average = sum(usability_ratings) / len(usability_ratings)
            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)
            score = (design_average + usability_average + content_average) / 3

            print(score)

            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()



            return HttpResponseRedirect(request.path_info)   
    context = {'project':project, 'ratings':ratings,'form':form,'rating_status':rating_status}   

    return render(request, 'users/project.html',context)