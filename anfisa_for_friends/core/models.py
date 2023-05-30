from django.db import models


class PublishedModel(models.Model):
    title: models.CharField = models.CharField(
        max_length=256,
        verbose_name='Название')
    is_published: models.BooleanField = models.BooleanField(
        default=True,
        verbose_name='Опубликовано')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
