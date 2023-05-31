from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import PublishedModel


class Category(PublishedModel):
    slug: models.SlugField = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг')
    output_order: models.PositiveSmallIntegerField = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='порядок отображения')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Topping(PublishedModel):
    slug: models.SlugField = models.SlugField(max_length=64,
        unique=True,
        verbose_name='слаг')

    class Meta:
        verbose_name = 'топпинг'
        verbose_name_plural = 'топпинги'


class Wrapper(PublishedModel):
    title: models.CharField = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Уникальное название обёртки, не более 256 символов')

    class Meta:
        verbose_name = 'обёртка'
        verbose_name_plural = 'обёртки'


class IceCream(PublishedModel):
    description: models.TextField = models.TextField(
        verbose_name='описание')
    wrapper: models.OneToOneField = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='обёртка'
    )
    category: models.ForeignKey = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='категория'
    )
    toppings: models.ManyToManyField = models.ManyToManyField(
        Topping,
        verbose_name='топпинг(и)')
    is_on_main: models.BooleanField = models.BooleanField(
        default=False,
        verbose_name='на главную')

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'
