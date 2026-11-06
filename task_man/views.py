from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.views.generic import TemplateView
from .forms import TaskForm


class TaskListView(TemplateView):
    template_name = 'task_man/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
   template_name = 'task_man/task_view.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
       return context


class TaskAddView(TemplateView):
    template_name = 'task_man/task_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
            )
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'task_man/task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type'],
            )
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})

class TaskUpdateView(TemplateView):
    template_name = 'task_man/task_update.html'

    def get_task(self):
        return get_object_or_404(Task, pk=self.kwargs['task_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_task()
        context['task'] = task
        context['form'] = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type,
        })
        return context

    def post(self, request, *args, **kwargs):
        task = self.get_task()
        form = TaskForm(request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', task_pk=task.pk)
        return render(
            request,
            self.template_name,
            {'form': form, 'task': task},
        )


class TaskDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        return redirect('task_view', task_pk=task.pk)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        task.delete()
        return redirect('task_list')