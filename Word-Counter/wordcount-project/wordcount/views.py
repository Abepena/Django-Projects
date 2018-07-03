from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are great!</h1>')