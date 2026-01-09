from rest_framework import serializers, viewsets, permissions
from .models import SystemSetting
from drf_spectacular.utils import extend_schema, extend_schema_view

class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = '__all__'

@extend_schema(tags=['System Configuration'])
@extend_schema_view(
    list=extend_schema(summary='List all system settings'),
    retrieve=extend_schema(summary='Get setting details'),
    update=extend_schema(summary='Update a setting'),
)
class SystemSettingViewSet(viewsets.ModelViewSet):
    queryset = SystemSetting.objects.all()
    serializer_class = SystemSettingSerializer
    permission_classes = [permissions.IsAdminUser] # Only admins can change settings

    def get_queryset(self):
        # Allow public read of public settings if needed, otherwise strict admin
        if not self.request.user.is_staff:
            return SystemSetting.objects.filter(is_public=True)
        return super().get_queryset()
