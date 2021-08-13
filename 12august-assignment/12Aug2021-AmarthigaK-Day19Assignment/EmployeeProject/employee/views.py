from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employee(request):
    return HttpResponse("Welcome to Employee Page")
def addemployee(request):
    return HttpResponse("Welcome to Add Employee Page")
def editemployee(request):
    return HttpResponse("Welcome to Edit Employee Page")
def deleteemployee(request):
    return HttpResponse("Welcome to Delete Employee Page")
def searchemployee(request):
    return HttpResponse("Welcome to Search Employee Page")