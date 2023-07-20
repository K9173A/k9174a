from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreateAPIView


app_name = 'auth'

urlpatterns = [
    path('token/', view=obtain_auth_token, name='token'),
    path('register/', view=UserCreateAPIView.as_view(), name='register'),
]
