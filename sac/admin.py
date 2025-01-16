from django.contrib import admin
from .models import Category, Recipe
# Register your models here.

# Criar classe para area administrativa do meu model

# CategoryAdmin: Esta classe herda de admin.ModelAdmin e permite personalizar a interface administrativa do modelo Category.


class CategoryAdmin(admin.ModelAdmin):
    ...

# Decorador para registrar um modelo no painel administrativo


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# Registrar o Modelo no Admin
admin.site.register(Category, CategoryAdmin)
