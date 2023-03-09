from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def warner(request):
    return HttpResponse('<marquee><h1>WARNER IS DELHI CAPTAIN</h1></marquee>')