from django.db import models
from slugify import slugify

class Day(models.Model):
    DAY_OF_WEEK = (
        (0,'ПН'),
        (1,'ВТ'),
        (2,'СР'),
        (3,'ЧТ'),
        (4,'ПТ'),
        (5,'СБ'),
        (6,'ВС'),

    )
    '''Model with date and day of week'''
    day = models.DateField()
    day_of_week = models.CharField(max_length=10, choices=DAY_OF_WEEK)

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self):
        return f'{self.day}'


class Group(models.Model):
    '''Model with number of students group'''
    number = models.CharField(max_length=6)
    slug = models.SlugField(max_length=10, default='empty')

    class Meta:
        verbose_name='Группа'
        verbose_name_plural='Группы'

    def __str__(self):
        return f'Группа {self.number}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.number)
        super(Group, self).save(*args, **kwargs)



class Cabinet(models.Model):
    '''Model with cabinets and their status'''
    number = models.CharField(max_length=5)

    class Meta:
        verbose_name='Кабинет'
        verbose_name_plural='Кабинеты'
    
    def __str__(self):
        return f'Кабинет {self.number}'


class Class(models.Model):
    '''Model with name of academic classes'''
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name='Пара'
        verbose_name_plural='Пары'
    
    def __str__(self):
        return self.name


class Timetable(models.Model):
    '''Model integraated all other models'''
    day = models.ForeignKey(Day, related_name='timetables', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='timetables', on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, related_name='timetables', on_delete=models.CASCADE)
    name_of_class = models.ForeignKey(Class, related_name='timetables', on_delete=models.CASCADE)
    number_of_class = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name='Расписание'
        verbose_name_plural='Расписание'

    def __str__(self):
        return f'{self.day.day} - {self.group.number} - {self.name_of_class.name}'