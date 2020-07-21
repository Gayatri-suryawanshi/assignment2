from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms         

# Create your views here.
def bmi(request):
     f1=forms.MyForm()
     return render(request,"bmi.html",{'form':f1})

def getdata(request):
    
    if request.method=="GET":
        weight=request.GET['weight']
        height=request.GET['height']
        w=float(weight)
        h=float(height)
        bmi=w/(h*h)
        return render(request,"valid.html",{"weight":w,"height":h,"b":bmi})


    if request.method=="POST":
        weight=request.POST['weight']
        hei=request.POST['height']
        w=float(weight)
        h=float(height)
        bmi=w/(h*h)
        return render(request,"valid.html",{"weight":w,"height":h,"b":bmi})


      