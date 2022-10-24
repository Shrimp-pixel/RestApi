from rest_framework.routers import DefaultRouter

from userapp.viewsets import UserViewSet
from todo.viewsets import TodoViewSet, ProjectViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('todo', TodoViewSet, basename='todo')
router.register('project', ProjectViewSet, basename='project')

urlpatterns = router.urls
