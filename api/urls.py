from django.urls import path
from .  import views

urlpatterns = [
    path('', views.GetStudents.as_view()),
]
