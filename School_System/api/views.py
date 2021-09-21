from django.shortcuts import render
from .serializer import StudentSerializer, TrainerSerializer ,CalenderSerializer,CourseSerializer
from rest_framework import serializers, viewsets
from student.models import Student
from trainer.models import Trainer
from calender.models import Calender
from courses.models import Courses



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CalenderViewSet(viewsets.ModelViewSet):
    queryset=Calender.objects.all()
    serializer_class=CalenderSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer


