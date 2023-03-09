from srh.views import *
from django.urls import path
app_name='j'
urlpatterns=[
    path('markram/',markram,name='markram'),
]