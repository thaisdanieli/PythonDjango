from django.shortcuts import render  # lê o arquivo e renderiza
from utils.sac.factory import make_recipe
from .models import Recipe

# Create your views here.

# Return HTTP Response


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'sac/pages/home.html',
                  context={'recipes': recipes,
                           })

# Recipe.objects.filter() é um método que permite filtrar os registros
# com base em condições específicas. Ele retorna um QuerySet
# category__id > o campo id da categoria associada à receita
# recipes recebe o resultado do filtro, que é um QuerySet contendo as
# receitas da categoria correspondente ao category_id


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'sac/pages/category.html',
                  context={'recipes': recipes,
                           })


def recipe(request, id):
    return render(request, 'sac/pages/recipe-view.html',
                  context={'recipe': make_recipe(),
                           'is_detail_page': True,
                           })


# Podemos filtrar dados usando uma Foreign Key (chave estrangeira)
# de determinado model.
# Para isso, usamos o nome do campo que representa a foreign key,
# dois underlines e o nome do campo no model estrangeiro
# (de onde vem a foreign key). Se o campo "category", de "Recipe",
# é uma foreign key para "Category",
# quando eu filtro category__name='Vegana', o que será retornado?
