# from school_system.student.models import Student
# from django.forms.forms import Form
from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.shortcuts import render


def register_student(request):
    form=StudentRegistrationForm()
    return render (request,"register_student.html",
    {"form":form})

