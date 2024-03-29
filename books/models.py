from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)

    authors = models.ManyToManyField(Author, related_name="books")
    tags = models.ManyToManyField("Tag", related_name="books")

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
