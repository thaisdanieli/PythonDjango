from django.shortcuts import render  # lê o arquivo e renderiza

# Create your views here.

# Return HTTP Response


def home(request):
    return render(request, 'sac/pages/home.html',
                  context={'name': 'Recipes', })


def recipe(request, id):
    return render(request, 'sac/pages/recipe-view.html',
                  context={'name': 'Thais Danieli', })
