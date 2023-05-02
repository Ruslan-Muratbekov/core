# Generated by Django 3.2.18 on 2023-05-02 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=228, verbose_name='Города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Город',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(max_length=528, verbose_name='Описание')),
                ('address', models.CharField(blank=True, max_length=1028, null=True, verbose_name='Адрес')),
                ('event_date', models.DateField(verbose_name='Дата')),
                ('event_time', models.TimeField(max_length=228, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятие',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FormatEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=528, verbose_name='Формат мероприятии')),
            ],
            options={
                'verbose_name': 'Форамат мероприятие',
                'verbose_name_plural': 'Форамат мероприятие',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ThemeOfEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=228, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тема мероприятии',
                'verbose_name_plural': 'Тема мероприятии',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubscribeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=258, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=258, verbose_name='Фамилия')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]
