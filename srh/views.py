from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def markram(request):
    return HttpResponse('<marquee><h1> AIDEN MARKRAM IS HYDERABAD CAPTAIN')