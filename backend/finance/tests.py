from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from properties.models import Property, Apartment
from contracts.models import Contract
from .models import Payment
from datetime import date, timedelta

class ReportsTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='password', email='a@a.com')
        self.client.force_authenticate(user=self.admin)
        
        self.prop = Property.objects.create(name='Prop', location='Loc', owner=self.admin)
        self.apt = Apartment.objects.create(property=self.prop, apartment_number='101', floor=1, monthly_rent=1000)
        self.contract = Contract.objects.create(
            tenant=self.admin, apartment=self.apt,
            start_date=date.today(), end_date=date.today() + timedelta(days=30),
            rent_amount=1000
        )

    def test_monthly_income_report(self):
        """Test that income report aggregates correctly"""
        Payment.objects.create(contract=self.contract, amount=500, payment_status='COMPLETED', payment_method='CASH')
        Payment.objects.create(contract=self.contract, amount=300, payment_status='COMPLETED', payment_method='ONLINE')
        Payment.objects.create(contract=self.contract, amount=200, payment_status='PENDING') # Should be ignored

        response = self.client.get('/api/v1/reports/monthly_income/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_income'], 800)

    def test_vacant_apartments_report(self):
        """Test vacant apartments count"""
        self.apt.status = 'VACANT'
        self.apt.save()
        
        # Create another rented one
        apt2 = Apartment.objects.create(property=self.prop, apartment_number='102', floor=1, monthly_rent=1000, status='RENTED')

        response = self.client.get('/api/v1/reports/vacant_apartments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_vacant'], 1)
        self.assertEqual(response.data['apartments'][0]['apartment_number'], '101')
