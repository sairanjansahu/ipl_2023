from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhawan(request):
    return HttpResponse('<marquee><h1>SHIKHAR DHAWAN IS PUNJAB CAPTAIN<h1></marquee>')