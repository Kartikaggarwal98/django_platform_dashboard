#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
import random


def index(request):
	context_dict={}
	return render(request,'home.html',context_dict)

def meets():
	context_dict={}
	return render(request,'calendar.html',context_dict)

