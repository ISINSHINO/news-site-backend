from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from news_app.permissions import UserEditPermission
from news_app.models import User
from news_app.serializers import UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.action in ['partial_update', 'update']:
            return [UserEditPermission(), ]
        return super().get_permissions()

    @action(detail=False, permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)