from django.core.management.base import BaseCommand
from core_settings.models import SystemSetting

class Command(BaseCommand):
    help = 'Seeds initial system settings'

    def handle(self, *args, **kwargs):
        settings = [
            {'key': 'MAINTENANCE_MODE', 'value': 'False', 'value_type': 'BOOLEAN', 'description': 'Enable system-wide maintenance mode'},
            {'key': 'VAT_PERCENTAGE', 'value': '15', 'value_type': 'INTEGER', 'description': 'Value Added Tax percentage'},
            {'key': 'SYSTEM_CURRENCY', 'value': 'SAR', 'value_type': 'STRING', 'description': 'Default currency for transactions', 'is_public': True},
            {'key': 'ALLOW_REGISTRATION', 'value': 'True', 'value_type': 'BOOLEAN', 'description': 'Allow new users to register'},
        ]

        for s in settings:
            obj, created = SystemSetting.objects.get_or_create(key=s['key'], defaults=s)
            if created:
                self.stdout.write(f"Created setting: {s['key']}")
            else:
                self.stdout.write(f"Setting exists: {s['key']}")

        self.stdout.write(self.style.SUCCESS('Settings seeded successfully!'))
