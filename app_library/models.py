from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.id}. {self.name} ({self.country}, {self.city})'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    biography = models.TextField()
    second_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=16, blank=True)
    personal_page = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    city = models.CharField(max_length=60, blank=True)
    country = models.CharField(max_length=60, blank=True)
    university = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
