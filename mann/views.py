from django.shortcuts import render
from django.contrib.auth.forms import UserRegisterForm, 
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,

# Create your views here.

def register (request):
  form = UserCreationForm(request.POST)
  return render(request,'users/register.html', {'form': form})

   
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
