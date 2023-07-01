from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, unique=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    first_name = models.CharField(verbose_name='Имя', max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, unique=True)
    authors = models.ManyToManyField(Author)
    poster = models.ImageField(verbose_name='poster', upload_to="img/")
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/')


