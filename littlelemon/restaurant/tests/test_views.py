from django.test import TestCase
from restaurant.models import Menu
from django.core.serializers import serialize
import json
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    client = APIClient()

    def setUp(self):
        self.menu1 = Menu.objects.create(title='Burger', price=12.50, inventory= 25)
        self.menu2 = Menu.objects.create(title='Fries', price=7.50, inventory= 20)

    def test_getall(self):
        response = self.client.get(reverse('menu_items'))
        menu = Menu.objects.all()
        serialized_menu = MenuSerializer(menu, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), json.loads(json.dumps(serialized_menu)))