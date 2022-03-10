from django.urls import path
from .views import *

urlpatterns = [
    path('', startups, name='startups'),
    path('project/<int:pk>', Project.as_view(), name='project'),
]