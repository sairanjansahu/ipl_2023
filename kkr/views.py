from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def iyer(request):
    return HttpResponse('<marquee><h1>IYER IS KOLKATA CAPTAIN</h1></marquee>')