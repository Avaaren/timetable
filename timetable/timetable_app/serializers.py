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
        fields = ['number',]

class TimetableSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    day = DaySerializer()
    name_of_class = ClassSerializer()
    cabinet = CabinetSerializer()

    class Meta:
        model = Timetable
        fields = ['id', 'number_of_class', 'group', 'day', 'name_of_class', 'cabinet']
    # Объект создается. Сделать проверку существование get() полей. Сделайть чтобы при занятии кабинета
    # в какой либо из дней нельзя было его на этот же день поставить
    def create(self, validated_data):
        group = Group.objects.get(number=validated_data['group']['number'])
        day = validated_data.pop('day')
        day = Day.objects.get_or_create(day=day['day'], day_of_week=day['day_of_week'])
        cabinet = Cabinet.objects.get(number=validated_data['cabinet']['number'])
        name_of_class = Class.objects.get(name=validated_data['name_of_class']['name'])
        number_of_class = validated_data['number_of_class']
        timetable = Timetable.objects.create(group=group, day=day[0], cabinet=cabinet, name_of_class=name_of_class, number_of_class=number_of_class)
        
        return timetable

    def update(self, instance, validated_data):
        instance.cabinet = Cabinet.objects.get(number=validated_data['cabinet']['number'])
        instance.name_of_class = Class.objects.get(name=validated_data['name_of_class']['name'])
        instance.save()
        return instance