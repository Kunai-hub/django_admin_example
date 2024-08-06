from django.test import TestCase
from django.urls import reverse


class WelcomeTest(TestCase):

    def test_welcome(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Добро пожаловать!')
