from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<button type="button">link drchrono</button>')

def success(request):
    return HttpResponse('Yay!! account linked')