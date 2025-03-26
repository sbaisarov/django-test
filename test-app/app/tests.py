from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Cart, CartItem

class APITestCase(TestCase):
    fixtures = ['test_data.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(username='testuser')
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

    def test_get_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Электроника')

    def test_get_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'Iphone 15')

    def test_get_cart(self):
        url = reverse('cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['product']['name'], 'Oppo A77')

    def test_add_to_cart(self):
        url = reverse('add-to-cart')
        data = {'product_id': 2, 'quantity': 1}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)

    def test_remove_from_cart(self):
        url = reverse('remove-from-cart', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 0)

    def test_update_cart_item(self):
        url = reverse('update-cart-item', args=[1])
        data = {'quantity': 3}
        print(url)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        cart_item = CartItem.objects.get(id=1)
        self.assertEqual(cart_item.quantity, 3)