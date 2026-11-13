from task_man.validators import MinLengthValidator, validate_forbidden_words
from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=100, validators=(MinLengthValidator(10),))
    description = models.TextField(validators=[validate_forbidden_words])
    status = models.ForeignKey('task_man.Status', on_delete=models.PROTECT)
    types = models.ManyToManyField('task_man.Type', related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.summary} - {self.created_at.strftime("%d.%m.%Y %H:%M")}'