from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class UserCreateAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.credentials = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'password'
        }

    def test_create_user(self) -> None:
        response = self.client.post(
            path=reverse(viewname='auth:register'),
            data=self.credentials,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_user(self) -> None:
        User.objects.create_user(**self.credentials)
        response = self.client.post(
            path=reverse(viewname='auth:register'),
            data=self.credentials,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_credentials(self) -> None:
        response = self.client.post(
            path=reverse(viewname='auth:register'),
            data={},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ObtainAuthTokenAPIViewTestCase(APITestCase):
    def test_obtain_token_by_existing_user(self) -> None:
        self.client.post(
            path=reverse(viewname='auth:register'),
            data={
                'username': 'test',
                'email': 'test@test.com',
                'password': 'password'
            },
            format='json'
        )
        response = self.client.post(
            path=reverse(viewname='auth:token'),
            data={
                'username': 'test',
                'password': 'password'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

    def test_obtain_token_by_nonexisting_user(self) -> None:
        response = self.client.post(
            path=reverse(viewname='auth:token'),
            data={
                'username': 'test2',
                'password': 'password'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
