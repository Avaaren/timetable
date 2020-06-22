from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView
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