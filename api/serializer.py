from django.db.models import fields
from rest_framework import serializers
from student.models import Student 
from trainer.models import Trainer
from calender.models import Calender
from courses.models import Courses



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=("first_name","last_name","age","nationality","gender","image")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name", "last_name","age","gender","nationality")


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calender
        fields=("venue", "event_id","event_name")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("course_name","course_code")