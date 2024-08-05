from django.db import models


class Item(models.Model):
    code = models.CharField(max_length=100, verbose_name='Артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
