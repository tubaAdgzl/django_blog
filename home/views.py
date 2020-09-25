from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
# Create your views here.

def home_views(request):
    return redirect("index")