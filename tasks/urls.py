from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    # Create a task
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    # Retrieve task list
    path('', views.TaskListView.as_view(), name='task_list'),
    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')
]
