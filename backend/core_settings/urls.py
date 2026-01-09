from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import SystemSettingViewSet

router = DefaultRouter()
router.register(r'settings', SystemSettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
