# pip install djangorestframework

# FILE: settings.py

INSTALLED_APPS = [
    'rest_framework',
]

# FILE: urls.py (main)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('blog.urls')),
]
