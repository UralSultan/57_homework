from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задач'

    def __str__(self):
        return f'{self.status}'