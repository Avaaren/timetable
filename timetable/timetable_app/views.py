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


class GetTimetableView(ListAPIView):

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


class GroupTimetableView(ListAPIView):

    serializer_class = TimetableSerializer

    def get_queryset(self):
        group = self.kwargs.get('group')
        group = get_object_or_404(Group, slug=group)
        return Timetable.objects.filter(group=group)


class AddTimetableView(CreateAPIView):

    #After adding - redirect to timetable list for group
    serializer_class = TimetableSerializer
    queryset = Timetable.objects.all()
    

class EditTimetableView(RetrieveUpdateAPIView):

    serializer_class = TimetableSerializer
    
    def get_object(self):
        return get_object_or_404(Timetable, pk=self.kwargs.get('pk'))


class DeleteTimetableView(RetrieveDestroyAPIView):

    serializer_class = TimetableSerializer

    def get_object(self):
        return get_object_or_404(Timetable, pk=self.kwargs.get('pk'))
