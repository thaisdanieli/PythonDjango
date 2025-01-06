from django.shortcuts import render  # lê o arquivo e renderiza
from utils.sac.factory import make_recipe

# Create your views here.

# Return HTTP Response


def home(request):
    return render(request, 'sac/pages/home.html',
                  context={'recipes': [make_recipe() for _ in range(6)],
                           })


def recipe(request, id):
    return render(request, 'sac/pages/recipe-view.html',
                  context={'recipe': make_recipe(),
                           'is_detail_page': True,
                           })
