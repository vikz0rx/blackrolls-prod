from django.shortcuts import render
from .models import *;

def index(request):
    sushi_menu = Food.objects.filter(kind=2)
    sushi_tempura_menu = Food.objects.filter(kind=4)
    sushi_black_menu = Food.objects.filter(kind=5)
    pizza_menu = Food.objects.filter(kind=1)
    salads_menu = Food.objects.filter(kind=6)
    drinks_menu = Food.objects.filter(kind=3)

    context = {
        'pizza': pizza_menu,
        'salads': salads_menu,
        'sushi': sushi_menu,
        'sushi_tempura': sushi_tempura_menu,
        'sushi_black': sushi_black_menu,
        'drinks': drinks_menu,
    }

    return render(request, 'index.html', context=context)