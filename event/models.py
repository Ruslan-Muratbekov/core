from django.db import models
from user.models import BaseAbstractModel, User


# Create your models here.

class ThemeOfEvent(models.Model):
    theme = models.CharField(max_length=228, null=False, blank=False, verbose_name='Тема')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name_plural = 'Тема мероприятии'
        verbose_name = 'Тема мероприятии'
        ordering = ['id']


class FormatEvent(models.Model):
    name = models.CharField(max_length=528, null=False, blank=False, verbose_name='Формат мероприятии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Форамат мероприятие'
        verbose_name = 'Форамат мероприятие'
        ordering = ['id']


class City(models.Model):
    city = models.CharField(max_length=228, null=False, blank=False, verbose_name='Города')

    def __str__(self):
        return f'{self.city}'

    class Meta:
        verbose_name_plural = 'Город'
        verbose_name = 'Город'
        ordering = ['id']


class Event(BaseAbstractModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=528, null=False, blank=False, verbose_name='Описание')
    address = models.CharField(max_length=1028, verbose_name='Адрес', null=True, blank=True)
    event_date = models.DateField(null=False, blank=False, verbose_name='Дата')
    event_time = models.TimeField(max_length=228, null=False, blank=False, verbose_name='Время')
    themeOfEvent = models.ForeignKey(ThemeOfEvent, on_delete=models.CASCADE, verbose_name='Тема мероприятии')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    formatEvent = models.ForeignKey(FormatEvent, on_delete=models.CASCADE, verbose_name='Формат мероприятии')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Мероприятие'
        verbose_name = 'Мероприятие'
        ordering = ['id']
