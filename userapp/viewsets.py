from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserSerializer, UserFullModelSerializer, DjangoUserBasicSerializer, DjangoUserModelSerializer
from django.contrib.auth.models import User as DjangoUser
from rest_framework import mixins


# class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserFullModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializer
        return UserFullModelSerializer


class DjangoUserViewSet(ListAPIView):
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserBasicSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return DjangoUserModelSerializer
        return DjangoUserBasicSerializer
