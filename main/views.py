# Create your views here.
import random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Restaurant

@csrf_exempt
def choose(request):
    """
    Handle HTTP POST Request
    """
    if request.method == 'POST':
        restaurants = Restaurant.objects.all().order_by('name')
        name_list = [restaurant.name for restaurant in restaurants]
        random.seed(None)
        result = random.choice(name_list)
        return HttpResponse(result)


