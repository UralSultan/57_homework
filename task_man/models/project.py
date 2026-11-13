from django.db import models


class Project(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-start_date']

    def __str__(self):
        return self.title