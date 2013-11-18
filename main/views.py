# Create your views here.
import random
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import Restaurant

@csrf_exempt
def choose(request):
    """
    Handle HTTP POST Request
    """
    if request.method == 'POST':
        option = request.POST['option']
        if option == 'Noon':
            restaurants = Restaurant.objects.filter(noon=1).exclude(evening=1)
        elif option == 'Evening':
            restaurants = Restaurant.objects.filter(noon=0).exclude(evening=0)
        else:
            restaurants = Restaurant.objects.all()
        name_list = [restaurant.name for restaurant in restaurants]
        print(name_list)
        random.seed(None)
        result = random.choice(name_list)
        return HttpResponse(result)


def index(request):
    """
    Render index page
    """
    context = {'option3': 'All'}
    current_hour = datetime.datetime.now().hour
    if current_hour < 13:
        context['option1'] = 'Noon'
        context['option2'] = 'Evening'
    else:
        context['option2'] = 'Evening'
        context['option1'] = 'Noon'

    return render(request, "index.html", context)


