from rest_framework import serializers
from .models import (
    Timetable,
    Group,
    Day,
    Class,
    Cabinet
)

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['number',]

class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = ['day', 'day_of_week']

class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ['name',]

class CabinetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cabinet
        fields = ['number', 'is_free']

class TimetableSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    day = DaySerializer(read_only=True)
    name_of_class = ClassSerializer(read_only=True)
    cabinet = CabinetSerializer(read_only=True)

    class Meta:
        model = Timetable
        fields = ['id', 'number_of_class', 'group', 'day', 'name_of_class', 'cabinet']
