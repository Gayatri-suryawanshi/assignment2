
from django.contrib import admin
from django.urls import path,include 
#from . import views

urlpatterns = [
    path('',include("bmi.urls")),
    path('bmi/',include("bmi.urls")),

]
