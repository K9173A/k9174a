from django.urls import path

from .views import (
    FilesListAPIView,
    FileRetrieveAPIView,
    FileUploadAPIView,
)


app_name = 'storage'

urlpatterns = [
    path('files/', view=FilesListAPIView.as_view(), name='files'),
    path('file/', view=FileRetrieveAPIView.as_view(), name='file'),
    path('upload/', view=FileUploadAPIView.as_view(), name='upload-file'),
]
