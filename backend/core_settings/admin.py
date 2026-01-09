from django.contrib import admin
from .models import SystemSetting

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'value_type', 'is_public', 'description')
    list_filter = ('value_type', 'is_public')
    search_fields = ('key', 'description')
