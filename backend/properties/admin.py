from django.contrib import admin
from .models import Property, Apartment

class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner', 'created_at')
    search_fields = ('name', 'location', 'owner__username')
    list_filter = ('created_at',)
    inlines = [ApartmentInline]

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('property', 'apartment_number', 'status', 'monthly_rent')
    list_filter = ('status', 'property')
    search_fields = ('apartment_number', 'property__name')
