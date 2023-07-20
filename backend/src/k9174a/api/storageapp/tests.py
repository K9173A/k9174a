from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from .models import File


class FileUploadAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='password', email='test@test.com')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        # self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    # def test_save_file_by_authenticated_user(self) -> None:
    #     file_name = 'test.txt'
    #     file = SimpleUploadedFile(name=file_name, content=b'test content')
    #     response = self.client.post(
    #         path=reverse(viewname='storage:upload-file'),
    #         data={'file': file},
    #         format='multipart',
    #         HTTP_CONTENT_DISPOSITION=f'Content-Disposition: inline; filename={file_name}'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     # Searching for file in database by id
    #     file = File.objects.get(id=response.data['id'])
    #     self.assertEqual(response.data['id'], str(file.id))
    #
    #     # Searching for file in database by its name (implies that there is no files with the same name)
    #     file = File.objects.filter(file__exact=file_name).first()
    #     self.assertEqual(response.data['id'], str(file.id))
    #
    # def test_save_invalid_file_by_authenticated_user(self) -> None:
    #     response = self.client.post(
    #         path=reverse(viewname='storage:upload-file'),
    #         format='multipart',
    #         HTTP_CONTENT_DISPOSITION=f'Content-Disposition: inline; filename=test.txt'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_save_file_by_unauthenticated_user(self) -> None:
        # todo: сделать так, чтобы проверка auth была до проверки файла
        # почему тут возвращает 201 CREATED?
        # self.client.credentials()
        file_name = 'test.txt'
        file = SimpleUploadedFile(name=file_name, content=b'test content')
        response = self.client.post(
            path=reverse(viewname='storage:upload-file'),
            data={'file': file},
            format='multipart',
            HTTP_CONTENT_DISPOSITION=f'Content-Disposition: inline; filename={file_name}'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_save_file_by_user_with_invalid_token(self) -> None:
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Token fake-token')
    #     response = self.client.post(path=reverse(viewname='storage:upload-file'))
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
