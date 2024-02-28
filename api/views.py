from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import StudentSerializer

class GetStudents(ListAPIView):
    queryset = Student.objects.all()
    serializer_class  = StudentSerializer

    # def get(self, request, *args, **kwargs):       
    #     return HttpResponse("Custom response for GET request", status=200)
