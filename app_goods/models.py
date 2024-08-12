from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    """
    Модель товара.
    """

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    weight = models.FloatField(verbose_name='Вес')
