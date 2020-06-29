from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
)
from .models import (
    Timetable,
    Group
)
from .serializers import TimetableSerializer
from .services.database_services import validate_day

class GetTimetableView(ListAPIView):
    """Getting list of all timetables"""
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


class GroupTimetableView(ListAPIView):
    """Getting list of timetables by group"""
    serializer_class = TimetableSerializer

    def get_queryset(self):
        group = self.kwargs.get('group')
        group = get_object_or_404(Group, slug=group)
        return Timetable.objects.filter(group=group)


class AddTimetableView(CreateAPIView):
    """Creating new timetable by post request"""
    #After adding - redirect to timetable list for group
    serializer_class = TimetableSerializer
    queryset = Timetable.objects.all()
    
    def create(self, request, *args, **kwargs):
        validate_day(request.data['day'])
        return super(CreateAPIView, self).create(request, *args, **kwargs)

class EditTimetableView(RetrieveUpdateAPIView):
    """Editing existed timetable (only cabinet and name of class)"""
    serializer_class = TimetableSerializer
    
    def get_object(self):
        return get_object_or_404(Timetable, pk=self.kwargs.get('pk'))


class DeleteTimetableView(RetrieveDestroyAPIView):
    """Deliting existed timetable"""
    serializer_class = TimetableSerializer

    def get_object(self):
        return get_object_or_404(Timetable, pk=self.kwargs.get('pk'))
