from django.contrib import admin
from .models import (
    Timetable,
    Group,
    Day,
    Class, 
    Cabinet
)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = '__all__'

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ['name',]
        list_filter = ['name',]

@admin.register(Cabinet)
class TimetableAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ['number', 'is_free']
        list_filter = ['number', 'is_free']

@admin.register(Day)
class TimetableAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ['day', 'day_of_week']
        list_filter = ['day', 'day_of_week']

@admin.register(Class)
class TimetableAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ['name',]
        list_filter = ['name',]
