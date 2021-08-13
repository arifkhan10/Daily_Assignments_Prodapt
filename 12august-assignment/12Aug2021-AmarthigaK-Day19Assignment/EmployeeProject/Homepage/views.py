from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Homepage(request):
    return HttpResponse("Welcome to my Home page")

def contactpage(request):
    return HttpResponse("Welcome to my Contact page")

def gallerypage(request):
    return HttpResponse("Welcome to my Gallery page")

