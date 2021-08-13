from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def company(request):
    return HttpResponse("Welcome to Company Page")
def addcompany(request):
    return HttpResponse("Welcome to Add Company Page")
def editcompany(request):
    return HttpResponse("Welcome to Edit Commpany Page")
def deletecompany(request):
    return HttpResponse("Welcome to Delete Company Page")
def searchcompany(request):
    return HttpResponse("Welcome to Search Company Page")