from django.db import models
from userapp.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=200, blank=True, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}-{self.url}'


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project}-{self.creator}'
