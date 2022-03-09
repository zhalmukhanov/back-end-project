from django.urls import path
from .views import *

urlpatterns = [
    path('', startups, name='startups'),
    path('project/<int:startup_id>/', project, name='project')
]