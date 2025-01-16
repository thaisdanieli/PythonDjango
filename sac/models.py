from django.db import models
# Vai utilizar o usuario como o autor da receita
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    # Dentro do django administrator na categoria este método vai retornar os nomes das categorias que estão cadastradas.
    def __str__(self):
        return self.name

# Como se fosse uma tabela da base de dados que recebe as informações do código para o banco de dados. Essa classe representa uma tabela chamada Recipe no banco de dados


class Recipe(models.Model):
    # CharField: Um campo de texto com limite de caracteres. max_length: Define o número máximo de caracteres que o campo pode armazenar.
    title = models.CharField(max_length=65)
    # Um campo usado para URLs amigáveis (por exemplo, minha-receita-deliciosa). Garante que o texto seja formatado para uso seguro em URLs.
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    # CharField: Define a unidade do tempo (por exemplo, "minutos", "horas")
    preparation_time_unit = models.CharField(max_length=65)
    # Número de porções que a receita rende.
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    # textfield - deixa o usuario escrever o quanto quiser
    preparation_steps = models.TextField()
    # BooleanField = Campo de escolha ou ele é True ou é False
    preparation_steps_is_html = models.BooleanField(default=False)
    # DateTimeField-True = No momento da criação ele gera uma data automatica
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True: Define que o valor será automaticamente atribuído no momento da criação do registro.
    update_at = models.DateTimeField(auto_now=True)
    # Um campo booleano para indicar se a receita está publicada ou não. default=False: Por padrão, a receita não será publicada.
    is_published = models.BooleanField(default=False)
    # ImageField: Um campo para armazenar imagens. upload_to: Define o caminho onde a imagem será armazenada - e salva a data do upload
    cover = models.ImageField(upload_to='recibes/covers/%Y/%m/%d/')
    # adiciona um campo ao modelo para criar uma relação entre a tabela atual e uma tabela chamada Category.
    # Define o que acontece quando um registro relacionado é excluido. SET_NULL: Quando uma categoria é excluída, o valor deste campo na receita é definido como NULL. null=True > Permite que o campo category seja nulo, ou seja, que uma receita não tenha nenhuma categoria associada.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    # Vai retornar o nome da receita no painel de listagem das Recipes
    def __str__(self):
        return self.title
