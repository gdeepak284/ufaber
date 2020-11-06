from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    url(r'^all-tasks/$', views.TaskIndexView.as_view(), name='allTasks'),
    url(r'^create-project/$', views.CreateProjectView.as_view(), name='createProject'),
    # path('project', views.projectDetail, name='projectDetails'),
    path(r'^my_project/<int:projectid>', views.projectDetail, name='myProject'),
    url(r'^new-task/$', views.CreateTaskView.as_view(), name='newTask'),
    url(r'^(?P<taskid>\d+)/detail/$', views.taskDetail, name='taskDetail'),
    path(r'^subtask/<int:subtaskid>/$', views.subTaskDetail, name='subTaskDetail'),
    path('edit-project/<projectid>', views.UpdateProjectView.as_view(), name='editProject'),
    url(r'^(?P<taskid>\d+)/edit/$', views.UpdateTaskView.as_view(), name='editTask'),
    url(r'^(?P<taskid>\d+)/delete/$', views.DeleteTaskView.as_view(), name='deleteTask'),
    path('delete-project/<projectid>', views.DeleteProjectView.as_view(), name='deleteProject'),
    url(r'^(?P<projectid>\d+)/createsubtask/$', views.CreateSubTaskView.as_view(), name='createSubTask'),

    # url(r'^(?P<taskid>\d+)/edit/$', views.UpdateProjectView.as_view(), name='editProject'),

]
