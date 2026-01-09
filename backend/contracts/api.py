from rest_framework import serializers, viewsets
from .models import Contract, models
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Serializer
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        apartment = data.get('apartment')

        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError("End date must be after start date.")

        # Check for Overlap
        overlapping_contracts = Contract.objects.filter(
            apartment=apartment,
            status='ACTIVE'
        ).filter(
            models.Q(start_date__lte=end_date) & models.Q(end_date__gte=start_date)
        )
        
        # If updating, exclude self
        if self.instance:
            overlapping_contracts = overlapping_contracts.exclude(pk=self.instance.pk)

        if overlapping_contracts.exists():
            raise serializers.ValidationError("This apartment already has an active contract for the selected duration.")

        return data

from drf_spectacular.utils import extend_schema, extend_schema_view

# ViewSet
@extend_schema(tags=['Leasing'])
@extend_schema_view(
    list=extend_schema(summary='List all contracts'),
    create=extend_schema(summary='Create a new lease contract'),
    retrieve=extend_schema(summary='Get contract details'),
)
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filterset_fields = ['tenant', 'apartment', 'status']
