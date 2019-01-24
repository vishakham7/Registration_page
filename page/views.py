# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
def detail(request):
	return HttpResponse("You're looking at question")