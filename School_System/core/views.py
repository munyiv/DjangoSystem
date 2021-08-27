
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from calender.models import Calender
# Create your views here.
def home(request):
    students=Student.objects
    trainers=Trainer.objects
    courses=Courses.objects.count()
    calendars=Calender.objects

    data ={ "students":students,"trainers":trainers,"courses":courses,calendars:"calendars"}
    return render (request,"home.html",data)



