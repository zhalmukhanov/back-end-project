from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from startup.models import Startup
from account.models import Startupper


# Create your views here.
def startups(request):
    if request.method == 'POST':
        startupper_id = request.POST.get('startupper')
        startupper = Startupper.objects.get(id=startupper_id)
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        initial_capital = request.POST.get('initial_capital')


        startupper.startup_set.create(
            title=title,
            description=description,
            category=category,
            initial_capital=initial_capital,
            accumulated_capital=0
        )

        startup_list = Startup.objects.order_by('-pk')
        startuppers = Startupper.objects.all()
        context = {
            'startups': startup_list,
            'startuppers': startuppers
        }
        return render(request, 'startups.html', context=context)
    else:
        startup_list = Startup.objects.order_by('-pk')
        startuppers = Startupper.objects.all()
        context = {
            'startups': startup_list,
            'startuppers': startuppers
        }
        return render(request, 'startups.html', context=context)

class Project(DetailView):
    model = Startup
    template_name = 'startup.html'
    context_object_name = 'project'
