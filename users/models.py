import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
	name = models.CharField(max_length=30, null=True, blank=True)
	surname = models.CharField(max_length=30, null=True, blank=True)
	bio = models.TextField(max_length=400, default='Empty bio yet')
	following = models.ManyToManyField(User, related_name='following', blank=True)
	created = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f"{self.user.username}'s profile"


	class Meta:
		ordering = ['-created']
	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.avatar.path)
		if img.height>150 or img.width>150:
			output_size=(150, 150) 
			img.thumbnail(output_size)
			img.save(self.avatar.path)

	


		