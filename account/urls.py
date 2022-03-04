from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('myroom/', myroom, name='myroom'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]