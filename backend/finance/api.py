from rest_framework import serializers, viewsets
from .models import Payment
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

from drf_spectacular.utils import extend_schema, extend_schema_view

# ViewSet
@extend_schema(tags=['Financials'])
@extend_schema_view(
    list=extend_schema(summary='List all payments'),
    create=extend_schema(summary='Record a new payment'),
    retrieve=extend_schema(summary='Get payment details'),
)
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_fields = ['contract', 'payment_status', 'payment_method']
