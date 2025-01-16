from django.shortcuts import render  # lê o arquivo e renderiza
from utils.sac.factory import make_recipe
from .models import Recipe

# Create your views here.

# Return HTTP Response


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'sac/pages/home.html',
                  context={'recipes': recipes,
                           })


def category(request):
    recipes = Recipe.objects.filter().order_by('-id')
    return render(request, 'sac/pages/home.html',
                  context={'recipes': recipes,
                           })


def recipe(request, id):
    return render(request, 'sac/pages/recipe-view.html',
                  context={'recipe': make_recipe(),
                           'is_detail_page': True,
                           })
