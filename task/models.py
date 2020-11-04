from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from taskmanagement import settings


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f"{self.name}"
