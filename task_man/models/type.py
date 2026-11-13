from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'

    def __str__(self):
        return f'{self.type}'
