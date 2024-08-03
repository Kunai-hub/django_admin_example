from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    county = models.CharField(max_length=60)
    is_active = models.BooleanField()
