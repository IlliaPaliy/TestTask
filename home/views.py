from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView	
from .models import User
from users.models import Profile
from django.contrib import messages


def home(request):
	return render(request, 'home/home.html')


class UsersListView(ListView):
	model = Profile
	template_name = 'home/home.html'
	context_object_name = 'users'
	
	def get_queryset(self):
		return Profile.objects.all().exclude(user = self.request.user)

class UsersDetailView(DetailView):
	model = User
	template_name = 'home/profile_detail.html'


	def get_object(self, **kwargs):
		pk = self.kwargs.get('pk')
		view_profile = User.objects.get(pk=pk)
		return view_profile

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		view_profile = self.get_object()
		current_profile = Profile.objects.get(user = self.request.user)
		if view_profile in current_profile.following.all():
			follow = True
		else:
			follow = False
		context['follow'] = follow
		return context


	def get_queryset(self):
		return Profile.following.filter(user = request.user)

def follow_action(request):
	if request.method == 'POST':
		current_profile = Profile.objects.get(user = request.user)
		pk = request.POST.get('profile_pk')
		profile = User.objects.get(pk=pk)

		if profile in current_profile.following.all():
			current_profile.following.remove(profile)
			messages.warning(request, f"Now you're not following {profile.username}." )

		else:
			current_profile.following.add(profile)
			messages.success(request, f"Now you're following {profile.username}." )

		return redirect(request.META.get('HTTP_REFERER'))
	return redirect('profile_info')

def random_picture(request):
	return render(request, 'home/picture.html')