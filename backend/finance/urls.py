from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PaymentViewSet
from .reports import ReportsViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)
router.register(r'reports', ReportsViewSet, basename='reports')

urlpatterns = [
    path('', include(router.urls)),
]
