from django.urls import path
from task_man import views

urlpatterns = [
    path('tasks/<int:task_pk>/', views.TaskView.as_view(), name='task_view'),
    path('tasks/<int:task_pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('tasks/<int:task_pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('projects/<int:project_pk>/tasks/add/', views.TaskAddView.as_view(), name='task_add'),
]