from django.conf import settings
from django.db import models


class Project(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='projects',blank=True,
        verbose_name='Участники',help_text='Выберите участников проекта. Снятие выбора удалит пользователя из проекта.')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-start_date']

    def __str__(self):
        return self.title
