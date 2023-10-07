from django.urls import path
from knox.views import LoginView, LogoutView, LogoutAllView

from .views import RegisterAPIView, ValidateTokenAPIView


app_name = 'auth'

urlpatterns = [
    path('login/', view=LoginView.as_view(), name='login'),
    path('logout/', view=LogoutView.as_view(), name='logout'),
    path('logoutall/', view=LogoutAllView.as_view(), name='logoutall'),
    path('register/', view=RegisterAPIView.as_view(), name='register'),
    path('validate/', view=ValidateTokenAPIView.as_view(), name='validate'),
]
