from django.shortcuts import render
from django.http import HttpResponse
from .models import Family
from.models import datetime

# Create your views here.
def welcome(request):
    return render(request,'welcome_family.html')
def family(request):
    family = Family.objects.all()
    context = {
            'family':family
        }
    return render(request,'welcome_family.html',context) 
     
