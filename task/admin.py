from __future__ import unicode_literals

from django.contrib import admin
from . models import Task, Project, SubTask

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(SubTask)

