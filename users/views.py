from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileAvatarUpdateForm
from django.views.generic import ListView
from .models import Profile

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')			
			return redirect('login')
	else:	
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	profile = Profile.objects.filter(user=request.user).first()
	followers = profile.following.all()
	context = {'followers' : followers}
	return render(request, 'users/profile.html', context)


@login_required
def change_profile(request):
	if request.method == 'POST':
		userform = UserUpdateForm(request.POST, instance=request.user)
		avatarform = ProfileAvatarUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		profileform = ProfileUpdateForm(request.POST, instance=request.user.profile)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			avatarform.save()
			messages.success(request, f'Account was updated')
			return redirect('profile')
	else:
		userform = UserUpdateForm(instance=request.user)
		avatarform = ProfileAvatarUpdateForm(instance=request.user.profile)
		profileform = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'userform' : userform,
		'profileform' : profileform,
		'avatarform' : avatarform
	}
	return render(request, 'users/change_profile.html', context)
