from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'NIR_UD/index.html')

def about(request):
    return render(request, 'NIR_UD/about.html')