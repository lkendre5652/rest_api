from .serializer import StudSerializer
from api.models import Student
from rest_framework import viewsets

class StudViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudSerializer

