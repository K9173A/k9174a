from django.urls import include, path


urlpatterns = [
    path('api/auth/', include(('api.authapp.urls', 'auth'), namespace='auth')),
    path('api/storage/', include(('api.storageapp.urls', 'storage'), namespace='storage')),
]
