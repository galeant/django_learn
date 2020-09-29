from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('ini index')

def detail(request):
    return HttpResponse('ini detail')

def update(request):
    return HttpResponse('ini update')

def delete(request):
    return HttpResponse('ini delete')