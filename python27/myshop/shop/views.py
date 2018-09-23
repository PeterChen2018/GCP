# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now=datetime.now()
    return render(request,"hi.html",locals())