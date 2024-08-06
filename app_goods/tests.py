from decimal import Decimal
from random import randint

from django.test import TestCase
from django.urls import reverse

from app_goods.models import Item


NUMBER_OF_ITEMS = 10


class ItemTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        for item in range(NUMBER_OF_ITEMS):
            Item.objects.create(
                code=item,
                price=Decimal(randint(1, 100))
            )

    def test_items_exist_at_desired_location(self):
        response = self.client.get('/goods/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/items_list.html')

    def test_items_number(self):
        response = self.client.get(reverse('items_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['items_list']) == NUMBER_OF_ITEMS)
