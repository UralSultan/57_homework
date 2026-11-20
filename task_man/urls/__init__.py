from .project_urls import urlpatterns as project_patterns
from .task_urls import urlpatterns as task_patterns


urlpatterns = (
    project_patterns
    + task_patterns
)