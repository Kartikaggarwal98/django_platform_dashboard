#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.models import UserProfile,Department
from forms import UserProfileForm, UserForm
import json
import requests
import random


def index(request):
	context_dict={}
	return render(request,'home.html',context_dict)

def meets():
	context_dict={}
	return render(request,'calendar.html',context_dict)

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save()

			profile.user = user
			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context_dict = {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
	}

	return render(request, "register.html", context_dict)

def user_login(request):

	if request.method == 'POST':
		username= request.POST.get('username')
		password=request.POST.get('password')

		user= authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/leaderboard/')
			else:
				return HttpResponse("Disabled account")
		else:
			return HttpResponse("Invalid login details!!!!")

	else:
		return render(request,"login.html",{})

def login():
	return render(request,'login.html')