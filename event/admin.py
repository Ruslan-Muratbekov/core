from django.contrib import admin
from .models import Event, FormatEvent


# Register your models here.
class FormatConfig(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class EventConfig(admin.ModelAdmin):
    list_display = ['id', 'title', 'event_date', 'event_time', 'themeOfEvent', 'formatEvent']
    list_display_links = ['id', 'title']


admin.site.register(Event, EventConfig)
admin.site.register(FormatEvent, FormatConfig)
