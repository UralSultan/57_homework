from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DeleteView, DetailView, FormView, UpdateView

from task_man.forms import TaskForm
from task_man.models import Project, Task


class TaskView(DetailView):
    model = Task
    template_name = 'task_man/task_view.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_pk'

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class TaskAddView(FormView):
    template_name = 'task_man/task_add.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def form_valid(self, form):
        task = form.save(commit=False)
        task.project = self.project
        task.save()
        form.save_m2m()
        return redirect('task_view', task_pk=task.pk)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_man/task_update.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_pk'

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_success_url(self):
        return reverse('task_view', kwargs={'task_pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_man/task_delete.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_pk'

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save(update_fields=['is_deleted'])
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project_id})
