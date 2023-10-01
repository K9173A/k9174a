from django.http import HttpRequest
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from .serializers import UserSerializer


class RegisterAPIView(generics.CreateAPIView):
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

        super(RegisterAPIView, self).perform_create(serializer)


# todo:
# class TokenValidateAPIView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request: HttpRequest) -> Response:
#         validity = None
#         return Response(status=status.HTTP_200_OK, data={'status': validity})


