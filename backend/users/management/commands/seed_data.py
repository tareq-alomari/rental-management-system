from django.core.management.base import BaseCommand
from users.models import User, Role
from properties.models import Property, Apartment
from contracts.models import Contract
from finance.models import Payment
from datetime import date, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # 1. Create Roles
        admin_role, _ = Role.objects.get_or_create(name='Admin', description='System Administrator')
        owner_role, _ = Role.objects.get_or_create(name='Owner', description='Property Owner')
        tenant_role, _ = Role.objects.get_or_create(name='Tenant', description='Rents apartments')

        # 2. Create Users
        admin, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com', 'role': admin_role})
        if not admin.check_password('admin123'):
            admin.set_password('admin123')
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()

        owner, _ = User.objects.get_or_create(username='owner1', defaults={'email': 'owner@example.com', 'role': owner_role})
        if not owner.check_password('password123'):
            owner.set_password('password123')
            owner.save()

        tenant, _ = User.objects.get_or_create(username='tenant1', defaults={'email': 'tenant@example.com', 'role': tenant_role})
        if not tenant.check_password('password123'):
            tenant.set_password('password123')
            tenant.save()

        # 3. Create Property
        prop, _ = Property.objects.get_or_create(
            name='Sunset Towers',
            owner=owner,
            defaults={'location': '123 Main St, Riyadh', 'description': 'Luxury apartments'}
        )

        # 4. Create Apartments
        apt1, _ = Apartment.objects.get_or_create(
            property=prop,
            apartment_number='101',
            defaults={'floor': 1, 'monthly_rent': 5000, 'status': 'VACANT'}
        )
        
        apt2, _ = Apartment.objects.get_or_create(
            property=prop,
            apartment_number='102',
            defaults={'floor': 1, 'monthly_rent': 6000, 'status': 'VACANT'}
        )

        # 5. Create Contract (This should trigger Signal to update status to RENTED)
        start_date = date.today()
        end_date = start_date + timedelta(days=365)
        
        contract, created = Contract.objects.get_or_create(
            tenant=tenant,
            apartment=apt1,
            defaults={
                'start_date': start_date,
                'end_date': end_date,
                'rent_amount': 5000,
                'status': 'ACTIVE'
            }
        )

        # 6. Create Payment
        if created:
             Payment.objects.create(
                 contract=contract,
                 amount=5000,
                 payment_method='ONLINE',
                 payment_status='COMPLETED'
             )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
