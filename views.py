

from django.shortcuts import render
from django.http import HttpResponse

def page1(request):
    return HttpResponse("This is page 1")

def page2(request):
    return HttpResponse("This is page 2")