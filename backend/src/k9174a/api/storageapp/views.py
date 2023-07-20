from mimetypes import guess_type
from pathlib import Path
from typing import Union

from django.conf import settings
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, FileResponse
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import File
from .permissions import IsRole
from .serializers import FileSerializer


class FilesListAPIView(generics.ListAPIView):
    # todo:
    # 1. Декодируем токен
    # 2. Ищем пользователя в БД
    # 3. Смотрим его роль
    # 4. По роли определяем, может ли он получить доступ к эндпоинту
    # authentication_classes =

    def get(self, request: HttpRequest, *args, **kwargs) -> Response:
        return Response(status=status.HTTP_200_OK)


class FileRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsRole(['*'])]
    serializer_class = FileSerializer

    def get_queryset(self) -> QuerySet:
        return File.objects.filter(
            Q(deleted_ts__is_null=True) &
            Q(id=self.request.GET.get('id'))
        )

    def get(self, request: HttpRequest, *args, **kwargs) -> Union[Response, FileResponse]:
        file = self.get_object()

        file_path = Path(settings.MEDIA_ROOT) / file['uid']
        if not file_path.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        mimetype, _ = guess_type(file_path, strict=True)
        if not mimetype:
            mimetype = 'text/html'

        return FileResponse(open(file_path, 'r'), content_type=mimetype)


class FileUploadAPIView(generics.CreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def post(self, request: HttpRequest, *args, **kwargs) -> Response:
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
