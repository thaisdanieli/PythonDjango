from django.db import models

# Create your models here.

# Como se fosse uma tabela da base de dados que recebe as informações do código para o banco de dados.


class Recipe(models.Model):
    # Campo de tempo que terá no máximo 65cm de largura
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    # textfield - deixa o usuario escrever o quanto quiser
    preparation_steps = models.TextField()
    # BooleanField = Campo de escolha ou ele é True ou é False
    preparation_steps_is_html = models.BooleanField(default=False)
    # DateTimeField-True = No momento da criação ele gera uma data automatica
    created_at = models.DateTimeField(auto_now_add=True)
    # DateTimeField-False = Campo de data e Ele será chamado quando o registro for atualizado
    update_at = models.DateTimeField(auto_now=False)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recibes/covers/%Y/%m%')
