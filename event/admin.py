from django.contrib import admin
from .models import Event, FormatEvent, ThemeOfEvent, City


# Register your models here.

class CityConfig(admin.ModelAdmin):
    list_display = ['id', 'city']
    list_display_links = ['id', 'city']


class ThemeConfig(admin.ModelAdmin):
    list_display = ['id', 'theme']
    list_display_links = ['id', 'theme']


class FormatConfig(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class EventConfig(admin.ModelAdmin):
    list_display = ['id', 'title', 'event_date', 'event_time', 'themeOfEvent', 'formatEvent', 'user']
    list_display_links = ['id', 'title']


admin.site.register(City, CityConfig)
admin.site.register(ThemeOfEvent, ThemeConfig)
admin.site.register(Event, EventConfig)
admin.site.register(FormatEvent, FormatConfig)
