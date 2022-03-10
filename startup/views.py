from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from startup.models import Startup
from account.models import Startupper

# Create your views here.
def startups(request):
    startup_list = Startup.objects.order_by('-pk')

    context ={
        'startups': startup_list
    }
    return render(request, 'startups.html', context = context)

def project(request, startup_id):
    startup = Startup.objects.get(pk = startup_id)
    return render(request, 'startup.html', {'startup': startup})

class Project(DetailView):
    model = Startup
    template_name = 'startup.html'
    context_object_name = 'project'