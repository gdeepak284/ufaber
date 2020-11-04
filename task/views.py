from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .mixins import LoginRequired, AuthorshipRequired
from .models import Task, Project


# Create your views here.
def projectDetail(request, projectid):
    project = get_object_or_404(Project, id=projectid)
    tasks = Task.objects.filter(project=project)
    print(tasks)
    context = {'project': project,
               'tasks': tasks}
    return render(request, 'project/detail_project.html', context)


class TaskIndexView(ListView):
    model = Task
    context_object_name = 'questions'
    template_name = 'task/tasks.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TaskIndexView, self).get_context_data(*args, **kwargs)
        task_list = Task.objects.all().order_by('-id')
        paginator = Paginator(task_list, 6)

        page = self.request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        context['allTaskTabActive'] = True
        context['tasks'] = tasks
        context['total'] = task_list.count()

        return context


class MyTaskView(TaskIndexView, LoginRequired):

    def get_context_data(self, *args, **kwargs):
        context = super(TaskIndexView, self).get_context_data(*args, **kwargs)
        task_list = Task.objects.filter(user=self.request.user)
        paginator = Paginator(task_list, 6)

        page = self.request.GET.get('page')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)

        context['tasks'] = tasks
        context['myTaskTabActive'] = True
        context['total'] = task_list.count()

        return context


def taskDetail(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    context = {'task': task}
    if task.user == request.user:
        context['myTaskTabActive'] = True
    else:
        context['allTaskTabActive'] = True

    return render(request, 'task/detail_task.html', context)


class CreateTaskView(LoginRequired, CreateView):
    template_name = 'task/create_task.html'
    model = Task
    fields = ['name', 'project', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)

    def get_success_url(self):
        return reverse('allTasks')


class CreateProjectView(LoginRequired, CreateView):
    template_name = 'project/create_project.html'
    model = Project
    fields = ['name', 'description', 'avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProjectView, self).form_valid(form)

    def get_success_url(self):
        return reverse('allTasks')


class UpdateTaskView(LoginRequired, AuthorshipRequired, UpdateView):
    template_name = 'task/edit_task.html'
    model = Task
    pk_url_kwarg = 'taskid'
    fields = ['name', 'description']

    def get_success_url(self):
        task = self.get_object()
        return reverse('taskDetail', kwargs={'taskid': task.pk})


class UpdateProjectView(LoginRequired, AuthorshipRequired, UpdateView):
    print("Hhehehdehded")
    template_name = 'project/edit_project.html'
    model = Project
    pk_url_kwarg = 'projectid'
    fields = ['name', 'description']

    def get_success_url(self):
        project = self.get_object()
        return reverse('myProject', kwargs={'projectid': project.pk})


class DeleteTaskView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'task/delete_task.html'
    model = Task
    pk_url_kwarg = 'taskid'

    def get_success_url(self):
        return reverse_lazy('allTasks')


class DeleteProjectView(LoginRequired, AuthorshipRequired, DeleteView):
    template_name = 'project/delete_project.html'
    model = Project
    pk_url_kwarg = 'projectid'

    def get_success_url(self):
        return reverse_lazy('allTasks')


class CreateSubTaskView(LoginRequired, CreateView):
    template_name = 'task/create_task.html'
    model = Task
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateSubTaskView, self).form_valid(form)

    def get_success_url(self):
        return reverse('allTasks')
