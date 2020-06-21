from rest_framework.generics import ListAPIView
from .models import Timetable
from .serializers import TimetableSerializer


class GetTimetableView(ListAPIView):

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

