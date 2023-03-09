from dd.views import *
from django.urls import path
app_name='b'
urlpatterns=[
    path('warner/',warner,name='warner')
]