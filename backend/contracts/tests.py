from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from properties.models import Property, Apartment
from .models import Contract
from datetime import date, timedelta

class ContractAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='password')
        self.client.force_authenticate(user=self.user)
        
        self.prop = Property.objects.create(name='Prop', location='Loc', owner=self.user)
        self.apt = Apartment.objects.create(property=self.prop, apartment_number='101', floor=1, monthly_rent=1000)
        self.url = '/api/v1/contracts/'

    def test_create_valid_contract(self):
        """Test creating a valid contract"""
        data = {
            'tenant': self.user.id,
            'apartment': self.apt.id,
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=365),
            'rent_amount': 1000
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.apt.refresh_from_db()
        self.assertEqual(self.apt.status, 'RENTED')

    def test_create_overlapping_contract_fails(self):
        """Test that overlapping contracts are rejected"""
        # Create first contract
        Contract.objects.create(
            tenant=self.user, apartment=self.apt, 
            start_date=date.today(), end_date=date.today() + timedelta(days=30), 
            rent_amount=1000, status='ACTIVE'
        )

        # Try to create second contract overlapping
        data = {
            'tenant': self.user.id,
            'apartment': self.apt.id,
            'start_date': date.today() + timedelta(days=5),
            'end_date': date.today() + timedelta(days=40),
            'rent_amount': 1000
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('active contract', str(response.data))
