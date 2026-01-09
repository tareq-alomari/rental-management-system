from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'apartment', 'start_date', 'end_date', 'status', 'rent_amount')
    list_filter = ('status', 'start_date', 'end_date')
    search_fields = ('tenant__username', 'apartment__apartment_number', 'apartment__property__name')
    date_hierarchy = 'start_date'
