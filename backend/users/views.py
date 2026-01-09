from rest_framework import viewsets, permissions
from .models import User, Role
from .serializers import UserSerializer, RoleSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema(tags=['Users & Roles'])
class RoleViewSet(viewsets.ModelViewSet):
    """
    Manage user roles (e.g., Admin, Owner, Tenant).
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

@extend_schema(tags=['Users & Roles'])
@extend_schema_view(
    list=extend_schema(summary='List all users'),
    create=extend_schema(summary='Register a new user'),
    retrieve=extend_schema(summary='Get user details'),
    update=extend_schema(summary='Update user details'),
    destroy=extend_schema(summary='Delete a user'),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
