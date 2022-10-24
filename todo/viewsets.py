from rest_framework import viewsets

from .filters import ProjectFilter, ToDoFilter
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer

from rest_framework.pagination import LimitOffsetPagination


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = ToDoFilter
    pagination_class = TodoLimitOffsetPagination


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination
