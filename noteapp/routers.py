from rest_framework.routers import DefaultRouter

from userapp.viewsets import UserViewSet
from todo.viewsets import TodoViewSet, ProjectViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('todo', TodoViewSet)
router.register('project', ProjectViewSet)

urlpatterns = router.urls
