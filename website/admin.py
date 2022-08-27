from django.contrib import admin

# Register your models here.
from .models import Event, ImportantDates

class EventAdmin(admin.ModelAdmin):
    search_fields = ['event_name', 'content']

admin.site.register(Event, EventAdmin)


class ImportantDatesAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(ImportantDates, ImportantDatesAdmin)