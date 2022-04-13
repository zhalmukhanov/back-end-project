from django.urls import path
from .views import *

urlpatterns = [
    path('', startups, name='startups'),
    path('add_startup/', add_startup, name='add_startup'),
    path('project/<int:pk>', startup_page, name='project'),
    path('main/', main_page, name='main_page'),
]