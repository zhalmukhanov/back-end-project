from django.http import HttpResponse
from django.shortcuts import render

def account(request):
    return HttpResponse("MyRoom")
