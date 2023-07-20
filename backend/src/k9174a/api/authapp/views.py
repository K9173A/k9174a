from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request: HttpRequest, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED)

    def perform_create(self, serializer: UserSerializer) -> None:
        email = serializer.validated_data['email']
        users = User.objects.filter(email=email)
        if users.exists():
            raise ValidationError(detail=f'User {email} already exists')

        super(UserCreateAPIView, self).perform_create(serializer)
