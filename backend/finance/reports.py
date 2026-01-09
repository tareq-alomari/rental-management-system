from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from properties.models import Apartment, Property
from finance.models import Payment
from contracts.models import Contract
from drf_spectacular.utils import extend_schema

class ReportsViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(tags=['Reports'], summary='Get Monthly Income Report')
    @action(detail=False, methods=['get'])
    def monthly_income(self, request):
        """
        FR-29: Report Monthly Income.
        """
        # Simple aggregation for all time, can be filtered by month request params
        total_income = Payment.objects.filter(payment_status='COMPLETED').aggregate(Sum('amount'))['amount__sum'] or 0
        
        # Breakdown by payment method
        breakdown = Payment.objects.filter(payment_status='COMPLETED').values('payment_method').annotate(total=Sum('amount'))
        
        return Response({
            'total_income': total_income,
            'breakdown': breakdown
        })

    @extend_schema(tags=['Reports'], summary='Get Vacant Apartments Report')
    @action(detail=False, methods=['get'])
    def vacant_apartments(self, request):
        """
        FR-31: Report Vacant Apartments.
        """
        vacant = Apartment.objects.filter(status='VACANT').values(
            'id', 'apartment_number', 'property__name', 'monthly_rent'
        )
        count = vacant.count()
        
        return Response({
            'total_vacant': count,
            'apartments': vacant
        })
    
    @extend_schema(tags=['Reports'], summary='Get Active Contracts Stats')
    @action(detail=False, methods=['get'])
    def contract_stats(self, request):
        """
        General Stats.
        """
        active = Contract.objects.filter(status='ACTIVE').count()
        expired = Contract.objects.filter(status='EXPIRED').count()
        return Response({
            'active_contracts': active,
            'expired_contracts': expired
        })
