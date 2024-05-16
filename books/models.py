from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self) -> str:
        return self.title
