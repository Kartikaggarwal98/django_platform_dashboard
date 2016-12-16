#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests

def index(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
	return render_to_response('authpage.html',context)