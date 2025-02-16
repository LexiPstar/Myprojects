from django.urls import reverse_lazy, reverse
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
