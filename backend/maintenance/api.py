from rest_framework import serializers, viewsets
from .models import MaintenanceRequest
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Serializer
class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

from drf_spectacular.utils import extend_schema, extend_schema_view

# ViewSet
@extend_schema(tags=['Maintenance'])
@extend_schema_view(
    list=extend_schema(summary='List maintenance requests'),
    create=extend_schema(summary='Submit a maintenance request'),
)
class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    filterset_fields = ['apartment', 'status']
