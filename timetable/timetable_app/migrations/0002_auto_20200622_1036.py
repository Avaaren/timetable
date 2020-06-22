# Generated by Django 3.0.7 on 2020-06-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='empty', max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='number_of_class',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
