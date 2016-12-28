from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	user_name=models.CharField(max_length=128,unique=True)
	user_email=models.EmailField(max_length=128,unique=True)
	user_phone=models.BigIntegerField(unique=True)
	profile_pic=models.ImageField(upload_to='profile_pic/')
	department=models.Charfield('Department',max_length=128)

	def __str__(self):
		return self.user_name

class Department(models.Model):
	dept_name=models.Charfield(max_length=128)

	def __str__(self):
		return self.dept_name
		