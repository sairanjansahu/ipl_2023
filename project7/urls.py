"""project7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import csk, dd, gt,kkr,lsg,mi,pk,rcb,rr,srh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csk/',include('csk.urls')),
    path('dd/',include('dd.urls')),
    path('gt/',include('gt.urls')),
    path('kkr/',include('kkr.urls')),
    path('lsg/',include('lsg.urls')),
    path('mi/',include('mi.urls')),
    path('pk/',include('pk.urls')),
    path('rcb/',include('rcb.urls')),
    path('rr/',include('rr.urls')),
    path('srh/',include('srh.urls')),
]
