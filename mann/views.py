from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from mann.models import Project

# Create your views here.

def home(request):
  context= {
    'projects': Project.objects.all()
  }
  return render(request, 'users/base.html', context)

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
