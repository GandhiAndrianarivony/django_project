from django.shortcuts import render
from django.http import HttpResponse

def homePageView(req):
    return HttpResponse("<h1>Hello World </h2>")

# Create your views here.
