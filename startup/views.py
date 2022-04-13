
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from startup.models import *
from account.models import *


# Create your views here.
def startups(request):
    if request.user.is_authenticated:
        is_authenticated = True
        username = request.user.username
    else:
        is_authenticated = False
        username = 'not logged in'

    page = 0
    paginator = 0
    startup_list = Startups.objects.order_by('-pk')
    startuppers = UserStartupper.objects.all()

    page = request.GET.get('page', 1)
    if request.GET.get('filter_category'):
        category = request.GET.get('filter_category')
        collected_amount = request.GET.get('collected_amount')

        startup = 0

        if category == 'All':
            startup = Startups.objects.order_by('-pk')
        else:
            startup = Startups.objects.filter(category=category).order_by('-pk')

        startups = list(startup)

        startup_list = []
        if collected_amount == '1':
            for i in startups:
                startup_list.append(i)
        elif collected_amount == '2':
            for i in startups:
                if i.percentage() > 0:
                    startup_list.append(i)
        elif collected_amount == '3':
            for i in startups:
                if i.percentage() >= 25:
                    startup_list.append(i)
        elif collected_amount == '4':
            for i in startups:
                if i.percentage() >= 50:
                    startup_list.append(i)
        elif collected_amount == '5':
            for i in startups:
                if i.percentage() >= 75:
                    startup_list.append(i)


    paginator = Paginator(startup_list, 5)
    try:
        startup_list = paginator.page(page)
    except PageNotAnInteger:
        startup_list = paginator.page(1)

    context = {
        'startups': startup_list,
        'startuppers': startuppers,
        'is_authenticated': is_authenticated,
        'username': username
    }
    return render(request, 'startups.html', context=context)


def startup_page(request, pk):
    if request.user.is_authenticated:
        is_authenticated = True
        username = request.user.username
    else:
        is_authenticated = False
        username = 'not logged in'

    startup = Startups.objects.get(pk=pk)

    context = {
        'project': startup,
        'is_authenticated': is_authenticated,
        'username': username
    }
    return render(request, 'startup.html', context=context)

def add_startup(request):
    user_id = request.user.id
    startupper = UserStartupper.objects.get(user_id=user_id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')
    initial_capital = request.POST.get('initial_capital')
    image = request.POST.get('image')

    startupper.startups_set.create(
        title=title,
        description=description,
        category=category,
        initial_capital=initial_capital,
        accumulated_capital=0
    )

    this_startup = Startups.objects.order_by('-pk')[0]
    url = '/startups/project/' + str(this_startup.pk)
    return HttpResponseRedirect(url)

def main_page(request):

    return render(request, 'main.html')
