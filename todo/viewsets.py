from rest_framework import viewsets

from .filters import ProjectFilter, ToDoFilter
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer, ProjectSerializerBase, TodoSerializerBase

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
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # filterset_class = ToDoFilter
    # pagination_class = TodoLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoSerializer

        return TodoSerializerBase


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerBase

    # def get_serializer_class(self):
    #    if self.request.method in ['GET']:
    #        return ProjectSerializer
#
#    return ProjectSerializerBase
# permission_classes = [SuperUserOnly, ]
# filterset_class = ProjectFilter
# pagination_class = ProjectLimitOffsetPagination
