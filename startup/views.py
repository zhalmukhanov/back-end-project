
from django.shortcuts import render
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
    project_list = request.GET.get(startup_id)
    startup = Startup.objects.get(id=project_list)
    return render(request, 'startup.html', startup)
