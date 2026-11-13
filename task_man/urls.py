from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects_view'),
    path('projects/add/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:project_pk>/tasks/add/', views.TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:task_pk>/', views.TaskView.as_view(), name='task_view'),
    path('tasks/<int:task_pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:task_pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
