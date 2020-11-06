from __future__ import unicode_literals

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User

from taskmanagement import settings
image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to=image_directory_path, storage=image_storage)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        return f"{self.name}"


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()