from django.urls import path
from .views import startups, add_startup, Project

urlpatterns = [
    path('', startups, name='startups'),
    path('add_startup/', add_startup, name='add_startup'),
    path('project/<int:pk>', Project.as_view(), name='project'),
]