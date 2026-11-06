from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'

    def __str__(self):
        return f'{self.status}'


class Type(models.Model):
    type = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

    def __str__(self):
        return f'{self.type}'


class Task(models.Model):
    summary = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.summary} - {self.created_at.strftime("%d.%m.%Y %H:%M")}'