from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user_name= models.CharField(max_length=128, null=False)
	profile_pic=models.ImageField(upload_to='profile_pic/',null=True)
	# department=models.ForeignKey('Department',max_length=128,null=True)
	isRegistered=models.BooleanField(null=False)

	def __str__(self):
		return self.user_name


