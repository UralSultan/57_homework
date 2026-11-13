from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from task_man.forms import ProjectModelForm
from task_man.models import Project


class ProjectsView(ListView):
    model = Project
    template_name = 'project/projects_view.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        projects = Project.objects.all()
        query = self.request.GET.get('q')
        if query:
            projects = projects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.select_related('status').prefetch_related('types')
        return context


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectModelForm
    template_name = 'project/project_create.html'
    success_url = reverse_lazy('projects_view')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectModelForm
    template_name = 'project/project_update.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('projects_view')
