from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Main Page")

def myroom(request):
    return HttpResponse("MyRoom")

def login(request):
    return HttpResponse("<h3>Enter login and password</h3><p>Don't have account yet? Register</p>")

def register(request):
    return HttpResponse("<h3>Fill information bellow </h3><p>Already have an account? Login</p>")
