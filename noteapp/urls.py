"""noteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny

from userapp.viewsets import UserViewSet, DjangoUserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='v1',
        description='Test api',
        contact=openapi.Contact(email='admin@mail.ru'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('noteapp.routers')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/<str:version>/users/', UserViewSet.as_view()),

    path('api/<str:version>/djangousers/', DjangoUserViewSet.as_view()),

    path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
]
