from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user= models.OneToOneField(User, null=True)
	profile_pic=models.ImageField(upload_to='profile_pic/')
	department=models.ForeignKey('Department',max_length=128,null=True)
	isRegistered=models.BooleanField(null=False)

	def __str__(self):
		return self.user_name

class Department(models.Model):
	dept_name=models.CharField(max_length=128)

	def __str__(self):
		return self.dept_name
