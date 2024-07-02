from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.

def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm

def logout_user(request):
   logout(request)
   return redirect("login")

@login_required
def view_profile(request):
    profile = get_object_or_404(Profile,user=request.user)
    context = {'profile':profile}
    return render(request,'users/profile.html',context)


@login_required
def update_profile(request):
   if request.method == 'POST':
       form = ProfileForm(request.POST, instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('tasks')
   else:
       form = ProfileForm(instance=request.user.profile)
  
   context = {'form': form}
   return render(request, 'users/profile-update-form.html', context)