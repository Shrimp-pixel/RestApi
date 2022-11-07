import json

import requests
from requests.auth import HTTPBasicAuth
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from userapp.models import User as ProjectUser
from userapp.viewsets import UserViewSet
from todo.viewsets import TodoViewSet, ProjectViewSet
from todo.models import Project, Todo


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'APushkin',
                                               'first_name': 'Александр',
                                               'last_name': 'Пушкин',
                                               'email': 'email@exampke.com',
                                               'birthday_year': 1799}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_admin(self):
        factory = APIRequestFactory()

        request = factory.post('/api/users/', {'username': 'APushkin',
                                               'first_name': 'Александр',
                                               'last_name': 'Пушкин',
                                               'email': 'email@exampke.com',
                                               'birthday_year': 1799}, format='json')

        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = ProjectUser.objects.create(username='APushkin',
                                          first_name='Александр',
                                          last_name='Пушкин',
                                          email='email@exampke.com',
                                          birthday_year=1799)

        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = ProjectUser.objects.create(username='APushkin',
                                          first_name='Александр',
                                          last_name='Пушкин',
                                          email='email@exampke.com',
                                          birthday_year=1799)

        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'last_name': 'Дюма',
                                                         'birthday_year': 1802})
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = ProjectUser.objects.create(username='APushkin',
                                          first_name='Александр',
                                          last_name='Пушкин',
                                          email='email@exampke.com',
                                          birthday_year=1799)

        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')

        client.login(username='admin', password='admin123456')

        response = client.put(f'http://127.0.0.1:8000/api/users/{user.id}/',
                              data={
                                  'username': 'APushkin',
                                  'first_name': 'Александр',
                                  'last_name': 'Дюма',
                                  'email': 'email@exampke.com',
                                  'birthday_year': 1802})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = ProjectUser.objects.get(id=user.id)
        self.assertEqual(user.last_name, 'Дюма')
        self.assertEqual(user.birthday_year, 1802)

        client.logout()


class TestProjectViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = ProjectUser.objects.create(username='APushkin',
                                          first_name='Александр',
                                          last_name='Пушкин',
                                          email='email@exampke.com',
                                          birthday_year=1799)

        project = Project.objects.create(name='Пиковая дама')
        project.users.set((user,))
        project.save()

        password = 'admin'
        admin = User.objects.create_superuser(username='admin', password=password)
        self.client.login(username='admin', password=password)

        response = self.client.put(f'/api/project/{project.id}/',
                                   data={'name': 'Руслан и Людмила',
                                         'users': project.users.first().id,
                                         'url': 'https://www.google.com/',
                                         })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'Руслан и Людмила')

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        user = mixer.blend(ProjectUser)

        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/project/{project.id}/',
                                   data={'name': 'Руслан и Людмила',
                                         'users': user.id,
                                         'url': 'https://www.google.com/',
                                         })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Project.objects.get(id=project.id)
        self.assertEqual(book.name, 'Руслан и Людмила')

    def test_get_detail(self):
        project = mixer.blend(Project, name='Алые паруса')
        user = mixer.blend(ProjectUser)

        response = self.client.get(f'/api/project/{project.id}/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['name'], 'Алые паруса')

    def test_get_detail_author(self):
        todo = mixer.blend(Todo, creator__username='username123')

        response = self.client.get(f'/api/todo/{todo.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_project = json.loads(response.content)
        self.assertEqual(response_project['creator']['username'], 'username123')
