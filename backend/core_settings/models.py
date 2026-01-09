from django.db import models

class SystemSetting(models.Model):
    KEY_TYPES = (
        ('STRING', 'String'),
        ('INTEGER', 'Integer'),
        ('BOOLEAN', 'Boolean'),
        ('FLOAT', 'Float'),
    )

    key = models.CharField(max_length=50, unique=True, help_text="Unique key for the setting (e.g. MAINTENANCE_MODE)")
    value = models.CharField(max_length=255, help_text="The value of the setting")
    description = models.TextField(blank=True, null=True)
    value_type = models.CharField(max_length=20, choices=KEY_TYPES, default='STRING')
    is_public = models.BooleanField(default=False, help_text="If true, accessible by public API")

    def __str__(self):
        return f"{self.key}: {self.value}"

    def get_typed_value(self):
        if self.value_type == 'INTEGER':
            return int(self.value)
        elif self.value_type == 'FLOAT':
            return float(self.value)
        elif self.value_type == 'BOOLEAN':
            return self.value.lower() in ('true', '1', 't')
        return self.value
