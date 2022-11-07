from rest_framework import serializers
from .models import Todo, Project
from userapp.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Todo
        fields = '__all__'


class TodoSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


# class ProjectSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Project
#        fields = '__all__'


class ProjectSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer()

    class Meta:
        model = Project
        fields = '__all__'
