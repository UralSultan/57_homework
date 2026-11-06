from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:task_pk>/', views.TaskView.as_view(), name='task_view'),
    path('task/add/', views.TaskAddView.as_view(), name='task_add'),
    path('task/<int:task_pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:task_pk>/delete/', views.TaskDeleteView.as_view(),name='task_delete')
]
