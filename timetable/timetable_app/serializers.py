from rest_framework import serializers
from .models import (
    Timetable,
    Group,
    Day,
    Class,
    Cabinet
)
import dateutil.parser
from datetime import datetime
from .services.database_services import check_cabinet


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
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(), allow_null=False, required=True, slug_field='number'
    )
    day = serializers.SlugRelatedField(
        queryset=Day.objects.all(), allow_null=False, required=True, slug_field='day'
    )
    name_of_class = serializers.SlugRelatedField(
        queryset=Class.objects.all(), allow_null=False, required=True, slug_field='name'
    )
    cabinet = serializers.SlugRelatedField(
        queryset=Cabinet.objects.all(), allow_null=False, required=True, slug_field='number'
    )

    class Meta:
        model = Timetable
        fields = ['id', 'number_of_class', 'group', 'day', 'name_of_class', 'cabinet']


    # Объект создается. Сделать проверку существование get() полей. Сделайть чтобы при занятии кабинета
    # в какой либо из дней нельзя было его на этот же день поставить
    def create(self, validated_data):
        group = validated_data['group']
        day = validated_data['day']
        cabinet = validated_data['cabinet']
        name_of_class = validated_data['name_of_class']
        number_of_class = validated_data['number_of_class']

        check_cabinet(cabinet, day, number_of_class)
        timetable = Timetable.objects.create(group=group, day=day, cabinet=cabinet, name_of_class=name_of_class, number_of_class=number_of_class)
        return timetable

    def update(self, instance, validated_data):
        instance.cabinet = Cabinet.objects.get(number=validated_data['cabinet']['number'])
        instance.name_of_class = Class.objects.get(name=validated_data['name_of_class']['name'])
        instance.save()
        return instance