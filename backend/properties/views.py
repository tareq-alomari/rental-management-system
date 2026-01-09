from rest_framework import viewsets
from .models import Property, Apartment
from .serializers import PropertySerializer, ApartmentSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema(tags=['Real Estate'])
@extend_schema_view(
    list=extend_schema(summary='List all properties'),
    create=extend_schema(summary='Add a new property'),
    retrieve=extend_schema(summary='Retrieve property details'),
)
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

@extend_schema(tags=['Real Estate'])
@extend_schema_view(
    list=extend_schema(summary='List all apartments'),
    create=extend_schema(summary='Add a new apartment unit'),
)
class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filterset_fields = ['property', 'status']
