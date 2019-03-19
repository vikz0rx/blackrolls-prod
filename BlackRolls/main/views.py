from django.shortcuts import render
from .models import *;

def index(request):
    sushi_menu = Food.objects.filter(kind=2)
    sushi_tempura_menu = Food.objects.filter(kind=4)
    pizza_menu = Food.objects.filter(kind=1)
    drinks_menu = Food.objects.filter(kind=3)

    context = {
        'pizza': pizza_menu,
        'sushi': sushi_menu,
        'sushi_tempura': sushi_tempura_menu,
        'drinks': drinks_menu,
    }

    return render(request, 'index.html', context=context)