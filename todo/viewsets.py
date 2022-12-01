from rest_framework import viewsets

from .filters import ProjectFilter, ToDoFilter
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, BasePermission


class SuperUserOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().filter(is_active=True)
    serializer_class = TodoSerializer
    # filterset_class = ToDoFilter
    # pagination_class = TodoLimitOffsetPagination


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [SuperUserOnly, ]
    # filterset_class = ProjectFilter
    # pagination_class = ProjectLimitOffsetPagination
