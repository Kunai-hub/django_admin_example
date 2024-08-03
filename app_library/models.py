from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    county = models.CharField(max_length=60)
    is_active = models.BooleanField()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    biography = models.TextField()
