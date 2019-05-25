from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def function(request):
    return render(request,"function.html")

def a(request):
    return render(request, "a.html")