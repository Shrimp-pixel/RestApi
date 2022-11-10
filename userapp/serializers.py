from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User as DjangoUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserFullModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email']
        fields = '__all__'


class DjangoUserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ['username', 'email']


class DjangoUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser']
