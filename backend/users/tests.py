from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Role

class AuthTests(APITestCase):
    def setUp(self):
        self.role = Role.objects.create(name='Tenant')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'test@example.com'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_token_obtain_pair(self):
        """Test JWT Token retrieval"""
        url = reverse('token_obtain_pair') # ensure this matches urls.py name
        data = {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_fail_invalid_creds(self):
        """Test JWT Token failure"""
        url = reverse('token_obtain_pair')
        data = {
            'username': self.user_data['username'],
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
