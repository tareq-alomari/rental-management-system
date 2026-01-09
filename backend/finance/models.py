from django.db import models
from contracts.models import Contract

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CASH', 'Cash'),
        ('ONLINE', 'Online'),
        ('BANK_TRANSFER', 'Bank Transfer'),
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='CASH')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    reference_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"
