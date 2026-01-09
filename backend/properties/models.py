from django.db import models
from django.conf import settings

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Properties"

class Apartment(models.Model):
    STATUS_CHOICES = (
        ('VACANT', 'Vacant'),
        ('RENTED', 'Rented'),
        ('MAINTENANCE', 'Under Maintenance'),
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='apartments')
    apartment_number = models.CharField(max_length=50)
    floor = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='VACANT')
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.property.name} - Apt {self.apartment_number}"
