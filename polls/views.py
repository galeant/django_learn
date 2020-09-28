from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requet):
    return HttpResponse("ini return dari views.py")