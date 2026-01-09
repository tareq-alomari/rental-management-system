from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Contract
from properties.models import Apartment

@receiver(post_save, sender=Contract)
def update_apartment_status_on_save(sender, instance, created, **kwargs):
    apartment = instance.apartment
    if instance.status == 'ACTIVE':
        apartment.status = 'RENTED'
    else:
        # Check if there are other active contracts (unlikely due to validation, but good safety)
        active_contracts = Contract.objects.filter(apartment=apartment, status='ACTIVE').exclude(pk=instance.pk).exists()
        if not active_contracts:
            apartment.status = 'VACANT'
    apartment.save()

@receiver(post_delete, sender=Contract)
def update_apartment_status_on_delete(sender, instance, **kwargs):
    apartment = instance.apartment
    active_contracts = Contract.objects.filter(apartment=apartment, status='ACTIVE').exists()
    if not active_contracts:
        apartment.status = 'VACANT'
    apartment.save()
