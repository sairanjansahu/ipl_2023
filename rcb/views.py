from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def faf(request):
    return HttpResponse('<marquee><h1> FAF DU PLESSIS IS BANGALORE CAPTAIN</h2></marquee>')