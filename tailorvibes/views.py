from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):  

    return render(request, "index.html")

def tailors(request):  
  
    return render(request, "tailors.html")

def hire(request):  
  
    return render(request, "hire.html")

def market(request):  
  
    return render(request, "market.html")