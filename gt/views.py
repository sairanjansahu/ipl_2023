from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hardhik(request):
    return HttpResponse('<marquee><h1>HARDHIK IS GUJURAT CAPTAIN</h1></marquee>')