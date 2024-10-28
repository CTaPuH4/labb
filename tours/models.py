from django.contrib.auth.models import User
from django.db import models

from .constants import (TITLE_MAX_LENGTH, TITLE_SHOWING_LENGTH)
from .managers import PublishedManager


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )

    class Meta:
        abstract = True


class Location(PublishedModel):
    country = models.CharField('Страна', max_length=TITLE_MAX_LENGTH)
    name = models.CharField('Название места', max_length=TITLE_MAX_LENGTH)

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return (f'{self.country}, {self.name}')[:TITLE_SHOWING_LENGTH]


class Tour(PublishedModel):
    title = models.CharField('Заголовок', max_length=TITLE_MAX_LENGTH)
    price = models.IntegerField('Цена')
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        verbose_name='Направление',
    )
    objects = models.Manager()
    published_objects = PublishedManager()
    image = models.ImageField('Фото', upload_to='tour_images', blank=True)
    subscribers = models.ManyToManyField(User,
                                         related_name='favorites',
                                         blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'тур'
        verbose_name_plural = 'Туры'
        default_related_name = 'tours'

    def __str__(self):
        return self.title[:TITLE_SHOWING_LENGTH]
