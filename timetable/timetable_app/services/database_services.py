from timetable_app.models import Day, Timetable
from rest_framework import serializers

import dateutil.parser as parser
from datetime import datetime


def validate_day(day):
    '''Creating day object if it is doesn't exist'''
    day = parser.parse(day).date()
    weekday = day.weekday()
    if not Day.objects.filter(day=day).exists():
        Day.objects.create(day=day, day_of_week=weekday)

def check_cabinet(cabinet, day, number_of_class):
    '''Checking is cabinet free at selected date and number of class'''
    if Timetable.objects.filter(day=day, cabinet=cabinet, number_of_class=number_of_class).exists():
        raise serializers.ValidationError("Cabinet is not free")
    else:
        return True
        