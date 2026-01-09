from rest_framework import serializers, viewsets
from .models import Notification
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

from drf_spectacular.utils import extend_schema, extend_schema_view

# ViewSet
@extend_schema(tags=['Notifications'])
@extend_schema_view(
    list=extend_schema(summary='List user notifications'),
    create=extend_schema(summary='Send a notification'),
)
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filterset_fields = ['user', 'is_read']
