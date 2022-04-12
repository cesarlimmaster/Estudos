from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('nome do livro', max_length=30)
    pages = models.IntegerField('quantidade de páginas')
    author = models.CharField('nome do autor', max_length=100, null=True)

    def __str__(self): return self.name