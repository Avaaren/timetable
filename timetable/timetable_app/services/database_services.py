from timetable_app.models import Day

import dateutil.parser as parser
from datetime import datetime


def validate_day(day):
    '''Creating day object if it is doesn't exist'''
    day = parser.parse(day).date()
    weekday = day.weekday()
    if not Day.objects.filter(day=day).exists():
        Day.objects.create(day=day, day_of_week=weekday)
        