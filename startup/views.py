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