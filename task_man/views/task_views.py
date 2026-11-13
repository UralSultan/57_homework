from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from task_man.models import Task
from django.views.generic import TemplateView, FormView
from task_man.forms import TaskForm


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

class TaskAddView(FormView):
    template_name = 'task_man/task_add.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save()
        return redirect('task_view', task_pk=task.pk)

# class TaskAddView(TemplateView):
#     template_name = 'task_man/task_add.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = TaskForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = Task.objects.create(
#                 summary=form.cleaned_data['summary'],
#                 description=form.cleaned_data['description'],
#                 status=form.cleaned_data['status'],
#             )
#
#             task.types.set(form.cleaned_data['types'])
#             return redirect('task_list')
#
#         return render(request, self.template_name, {'form': form})


class TaskUpdateView(FormView):
    template_name = 'task_man/task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task,pk=self.kwargs['task_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.task, key)
        initial['types'] = self.task.types.all()
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop('types')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.types.set(types)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('task_view', kwargs={'task_pk': self.task.pk})


# class TaskUpdateView(TemplateView):
#     template_name = 'task_man/task_update.html'
#
#     def get_task(self):
#         return get_object_or_404(Task, pk=self.kwargs['task_pk'])
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         task = self.get_task()
#         context['task'] = task
#         context['form'] = TaskForm(initial={
#             'summary': task.summary,
#             'description': task.description,
#             'status': task.status,
#             'types': task.types.all(),
#         })
#         return context
#
#     def post(self, request, *args, **kwargs):
#         task = self.get_task()
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task.summary = form.cleaned_data['summary']
#             task.description = form.cleaned_data['description']
#             task.status = form.cleaned_data['status']
#             task.save()
#             task.types.set(form.cleaned_data['types'])
#             return redirect('task_view', task_pk=task.pk)
#         return render(
#             request,
#             self.template_name,
#             {'form': form, 'task': task},
#         )


class TaskDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        return redirect('task_view', task_pk=task.pk)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        task.delete()
        return redirect('task_list')