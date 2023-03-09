from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('<marquee><h1>MSD IS CSK CAPTAIN</h1></marquee>')