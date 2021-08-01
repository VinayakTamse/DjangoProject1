from django.http import HttpResponse
from django.shortcuts import render

def Home(request):

    return render(request, 'mysite/home.html')

def About(request):

    return render(request, 'mysite/about.html')

