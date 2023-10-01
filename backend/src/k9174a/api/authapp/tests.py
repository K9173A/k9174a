import base64

from django.urls import reverse
from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


def get_basic_auth_header(username: str, password: str) -> str:
    return 'Basic {}'.format(base64.b64encode(f'{username}:{password}'.encode('ascii')).decode())


class TestUserData:
    username = 'test'
    email = 'test@test.com'
    password = 'password'

    @staticmethod
    def as_dict():
        return {
            'username': TestUserData.username,
            'email': TestUserData.email,
            'password': TestUserData.password
        }


class UserCreateAPIViewTestCase(APITestCase):
    def test_create_user(self) -> None:
        response = self.client.post(
            path=reverse(viewname='auth:register'),
            data=TestUserData.as_dict(),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_user(self) -> None:
        User.objects.create_user(**TestUserData.as_dict())
        response = self.client.post(
            path=reverse(viewname='auth:register'),
            data=TestUserData.as_dict(),
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


class LoginAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_login(self) -> None:
        User.objects.create_user(**TestUserData.as_dict())
        self.client.credentials(HTTP_AUTHORIZATION=get_basic_auth_header(TestUserData.username, TestUserData.password))
        response = self.client.post(path=reverse(viewname='auth:login'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

    def test_login_user_without_auth_header(self) -> None:
        self.client.credentials()
        response = self.client.post(path=reverse(viewname='auth:login'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)

    def test_login_nonexisting_user(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION=get_basic_auth_header('doesnt', 'exist'))
        response = self.client.post(path=reverse(viewname='auth:login'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)


class LogoutAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_logout(self) -> None:
        User.objects.create_user(**TestUserData.as_dict())
        self.client.credentials(HTTP_AUTHORIZATION=get_basic_auth_header(TestUserData.username, TestUserData.password))
        response = self.client.post(path=reverse(viewname='auth:login'))

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {response.data["token"]}')
        response = self.client.post(path=reverse(viewname='auth:logout'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)

    def test_logout_without_auth_header(self) -> None:
        self.client.credentials()
        response = self.client.post(path=reverse(viewname='auth:logout'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)

    def test_logout_with_fake_token(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION='Token fake-token')
        response = self.client.post(path=reverse(viewname='auth:logout'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)


class LogoutAllAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_logout_all(self) -> None:
        User.objects.create_user(**TestUserData.as_dict())
        self.client.credentials(HTTP_AUTHORIZATION=get_basic_auth_header(TestUserData.username, TestUserData.password))

        for _ in range(3):
            response = self.client.post(path=reverse(viewname='auth:login'))
            self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)

        self.assertEqual(AuthToken.objects.count(), 3)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {response.data["token"]}')
        response = self.client.post(path=reverse(viewname='auth:logoutall'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(AuthToken.objects.count(), 0)

    def test_logout_all_without_auth_header(self) -> None:
        self.client.credentials()
        response = self.client.post(path=reverse(viewname='auth:logoutall'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)

    def test_logout_all_with_fake_token(self) -> None:
        self.client.credentials(HTTP_AUTHORIZATION='Token fake-token')
        response = self.client.post(path=reverse(viewname='auth:logoutall'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, msg=response.data)
