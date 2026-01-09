from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Property, Apartment

class PropertyTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='password')
        self.client.force_authenticate(user=self.user)
        self.url = '/api/v1/properties/'

    def test_create_property(self):
        """Test creating a property"""
        data = {'name': 'New Tower', 'location': 'Jeddah', 'owner': self.user.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 1)

    def test_get_properties_list(self):
        """Test listing properties"""
        Property.objects.create(name='P1', location='L1', owner=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_unauthenticated_access(self):
        """Test unauthenticated access denial"""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
